#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is part of Androwarn.
#
# Copyright (C) 2012, 2019, Thomas Debize <tdebize at mail.com>
# All rights reserved.
#
# Androwarn is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Androwarn is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Androwarn.  If not, see <http://www.gnu.org/licenses/>.

# Global imports
import logging

# Androwarn modules import
from warn.core.core import *
from warn.util.util import *

# Logguer
log = logging.getLogger('log')

def detect_Connectivity_Manager_leakages(x):
    """
        @param x : a Analysis instance
    
        @rtype : a list strings for exemple [ 'This application makes phone calls', "This application sends an SMS message 'Premium SMS' to the '12345' phone number" ]
    """
    
    method_listing = [
            ("getActiveNetworkInfo()",      "This application reads details about the currently active data network"),
            ("isActiveNetworkMetered()",    "This application tries to find out if the currently active data network is metered")
    ]
    method_listing_cn = [
            ("getActiveNetworkInfo()",      "读取当前活动网络数据的信息"),
            ("isActiveNetworkMetered()",    "检测当前活动的网络数据是否被计量")
    ]

    
    class_name = 'Landroid/net/ConnectivityManager'
    
    return structural_analysis_search_method_bulk(class_name, method_listing_cn, x)
 
def detect_WiFi_Credentials_lookup(x) :
    """
        @param x : a Analysis instance
        
        @rtype : a list of formatted strings
    """
    # This functions aims some HTC android devices 
    # Several HTC devices suffered from a bug allowing to dump wpa_supplicant.conf file containing clear text credentials
    # http://www.kb.cert.org/vuls/id/763355
    
    formatted_str = []
    
    structural_analysis_results = structural_analysis_search_method("Landroid/net/wifi/WifiConfiguration", "toString", x)
    for registers in data_flow_analysis(structural_analysis_results, x):
        local_formatted_str = "This application reads the WiFi credentials"
        local_formatted_str_cn = "读取WiFi证书"
        
        if not(local_formatted_str_cn in formatted_str) :
            formatted_str.append(local_formatted_str_cn)

        
    return sorted(formatted_str)

def gather_connection_interfaces_exfiltration(x) :
    """
        @param x : a Analysis instance
    
        @rtype : a list strings for the concerned category, for exemple [ 'This application makes phone calls', "This application sends an SMS message 'Premium SMS' to the '12345' phone number" ]
    """
    result = []
    
    result.extend( detect_WiFi_Credentials_lookup(x) )
    result.extend( detect_Connectivity_Manager_leakages(x) )
    
    return result
