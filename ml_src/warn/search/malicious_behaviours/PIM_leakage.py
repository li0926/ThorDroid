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
from warn.util.util import *

# Logguer
log = logging.getLogger('log')

def detect_content_provider_access(x):
    """
        @param x : a Analysis instance
        
        @rtype : a list of formatted strings
    """
    formatted_str = []
    
    string_listing = [  ("content://sms",                                   "This application accesses the SMS list"),
                        ("content://mms-sms",                               "This application accesses the SMS/MMS list"),
                        ("content://mms",                                   "This application accesses the MMS list"),
                        ("content://com.google.contacts",                   "This application accesses the contacts list"),
                        ("content://com.android.contacts",                  "This application accesses the contacts list"),
                        ("content://contacts",                              "This application accesses the contacts list"),
                        ("content://downloads",                             "This application accesses the downloads folder"),
                        ("content://com.android.calendar",                  "This application accesses the calendar"),
                        ("content://calendar",                              "This application accesses the calendar"),
                        ("content://call_log",                              "This application accesses the call log"),
                        ("content://com.android.fmradio",                   "This application accesses the FM radio"),
                        ("content://com.android.browser",                   "This application accesses the native browser data"),
                        ("content://com.android.providers.voicemail",       "This application accesses the voicemail"),
                        ("content://sync",                                  "This application accesses the synchronisation history"),
                        ("content://com.android.bluetooth.opp/",            "This application accesses the Bluetooth"),
                        ("content://com.android.email.provider",            "This application accessed the mail application data"),
                        ("content://com.android.email.attachmentprovider",  "This application accessed the mail application data"),
                        ("content://com.android.browser",                   "This application accesses the native browser data")
    ]
    string_listing_cn= [  ("content://sms",                                  "读取短信列表"),
                        ("content://mms-sms",                               "读取短信和彩信列表"),
                        ("content://mms",                                   "读取彩信列表"),
                        ("content://com.google.contacts",                   "读取通讯录"),
                        ("content://com.android.contacts",                  "读取通讯录"),
                        ("content://contacts",                              "读取通讯录"),
                        ("content://downloads",                             "读取下载文件夹"),
                        ("content://com.android.calendar",                  "读取日历"),
                        ("content://calendar",                              "读取日历"),
                        ("content://call_log",                              "读取通话记录"),
                        ("content://com.android.fmradio",                   "读取广播"),
                        ("content://com.android.browser",                   "读取原生浏览器数据"),
                        ("content://com.android.providers.voicemail",       "读取语音信箱"),
                        ("content://sync",                                  "读取同步历史"),
                        ("content://com.android.bluetooth.opp/",            "读取蓝牙"),
                        ("content://com.android.email.provider",            "读取邮箱应用数据"),
                        ("content://com.android.email.attachmentprovider",  "读取邮箱应用数据"),
                        ("content://com.android.browser",                   "读取原生浏览器数据")
    ]
    
    return structural_analysis_search_string_bulk(string_listing_cn, x)


def detect_clipboard_manager_calls(x):
    """
        @param x : a Analysis instance
        
        @rtype : a list of formatted strings
    """
    method_listing = [
            ("getPrimaryClip",              "This application accesses data stored in the clipboard"),
            ("getText",                     "This application accesses data stored in the clipboard"),
            ("hasPrimaryClip",              "This application accesses data stored in the clipboard"),
            ("hasText",                     "This application accesses data stored in the clipboard"),
    ]
    method_listing_cn = [
            ("getPrimaryClip",              "访问剪切板中的数据"),
            ("getText",                     "访问剪切板中的数据"),
            ("hasPrimaryClip",              "访问剪切板中的数据"),
            ("hasText",                     "访问剪切板中的数据"),
    ]
    
    class_name = "Landroid/content/ClipboardManager"
    
    return structural_analysis_search_method_bulk(class_name, method_listing_cn, x)

def gather_PIM_data_leakage(x):
    """
        @param x : a Analysis instance
    
        @rtype : a list strings for the concerned category, for exemple [ 'This application makes phone calls', "This application sends an SMS message 'Premium SMS' to the '12345' phone number" ]
    """
    result = []
    
    result.extend( detect_content_provider_access(x) )
    result.extend( detect_clipboard_manager_calls(x) )
        
    return result
