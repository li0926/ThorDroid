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

def detect_telephony_gsm_GsmCellLocation(x):
    """
        @param x : a Analysis instance
    
        @rtype : a list strings for exemple [ 'This application makes phone calls', "This application sends an SMS message 'Premium SMS' to the '12345' phone number" ]
    """
    
    method_listing = [
            ("getLac()",    "This application reads the Location Area Code value"),
            ("getCid()",    "This application reads the Cell ID value")
    ]
    method_listing_cn = [
            ("getLac()",    "读取位置区码"),
            ("getCid()",    "读取Cid码")
    ]
    
    class_name = 'Landroid/telephony/gsm/GsmCellLocation'
    
    return structural_analysis_search_method_bulk(class_name, method_listing_cn, x)

def detect_Telephony_Manager_Leakages(x) :
    """
        @param x : a Analysis instance
    
        @rtype : a list strings for exemple [ 'This application makes phone calls', "This application sends an SMS message 'Premium SMS' to the '12345' phone number" ]
    """
    
    method_listing = [
            ("getCallState()",              "This application reads the phone's current state"),
            ("getCellLocation()",           "This application reads the current location of the device"),
            ("getDataActivity()",           "This application reads the type of activity on a data connection"),
            ("getDataState()",              "This application reads the current data connection state"),
            ("getDeviceId()",               "This application reads the unique device ID, i.e the IMEI for GSM and the MEID or ESN for CDMA phones"),
            ("getDeviceSoftwareVersion()",  "This application reads the software version number for the device, for example, the IMEI/SV for GSM phones"),
            ("getLine1Number()",            "This application reads the phone number string for line 1, for example, the MSISDN for a GSM phone"),
            ("getNeighboringCellInfo()",    "This application reads the neighboring cell information of the device"),
            ("getNetworkCountryIso()",      "This application reads the ISO country code equivalent of the current registered operator's MCC (Mobile Country Code)"),
            ("getNetworkOperator()",        "This application reads the numeric name (MCC+MNC) of current registered operator"),
            ("getNetworkOperatorName()",    "This application reads the operator name"),
            ("getNetworkType()",            "This application reads the radio technology (network type) currently in use on the device for data transmission"),
            ("getPhoneType()",              "This application reads the device phone type value"),
            ("getSimCountryIso()",          "This application reads the ISO country code equivalent for the SIM provider's country code"),
            ("getSimOperator()",            "This application reads the MCC+MNC of the provider of the SIM"),
            ("getSimOperatorName()",        "This application reads the Service Provider Name (SPN)"),
            ("getSimSerialNumber()",        "This application reads the SIM's serial number"),
            ("getSimState()",               "This application reads the constant indicating the state of the device SIM card"),
            ("getSubscriberId()",           "This application reads the unique subscriber ID, for example, the IMSI for a GSM phone"),
            ("getVoiceMailAlphaTag()",      "This application reads the alphabetic identifier associated with the voice mail number"),
            ("getVoiceMailNumber()",        "This application reads the voice mail number")
    ]
    method_listing_cn = [
            ("getCallState()",              "读取手机状态并监听手机来电状态"),
            ("getCellLocation()",           "读取设备当前位置信息"),
            ("getDataActivity()",           "读取数据连接中的activity的类型"),
            ("getDataState()",              "读取数据连接状态"),
            ("getDeviceId()",               "读取唯一的设备ID(如 IMEI、MEID)"),
            ("getDeviceSoftwareVersion()",  "读取设备的软件版本号(如 GSM手机的 IMEI/SV)"),
            ("getLine1Number()",            "读取设备的手机号码"),
            ("getNeighboringCellInfo()",    "读取周围基站的信息"),
            ("getNetworkCountryIso()",      "读取网络运营商国家码"),
            ("getNetworkOperator()",        "读取MCC和跨国公司的注册网络运营商"),
            ("getNetworkOperatorName()",    "读取网络运营商名称"),
            ("getNetworkType()",            "获取当前数据传输使用的网络类型(2/3/4G/Wifi..)"),
            ("getPhoneType()",              "读取设备类型"),
            ("getSimCountryIso()",          "读取与SIM卡提供商的国家/地区代码等效的ISO国家/地区代码"),
            ("getSimOperator()",            "读取SIM卡提供商的MCC+MNC"),
            ("getSimOperatorName()",        "读取服务提供商名称(SPN)"),
            ("getSimSerialNumber()",        "读取SIM卡的序列号"),
            ("getSimState()",               "读取指示设备SIM卡状态的常量"),
            ("getSubscriberId()",           "读取手机的IMSI号"),
            ("getVoiceMailAlphaTag()",      "读取与语音邮件号码关联的字母标识符"),
            ("getVoiceMailNumber()",        "读取语音邮件号码")
    ]
    
    class_name = 'Landroid/telephony/TelephonyManager'
    
    return structural_analysis_search_method_bulk(class_name, method_listing_cn, x)

def gather_telephony_identifiers_leakage(x) :
    """
        @param x : a Analysis instance
    
        @rtype : a list strings for the concerned category, for exemple [ 'This application makes phone calls', "This application sends an SMS message 'Premium SMS' to the '12345' phone number" ]
    """
    result = []

    result.extend( detect_Telephony_Manager_Leakages(x) )
    result.extend( detect_telephony_gsm_GsmCellLocation(x) )
    
    return result