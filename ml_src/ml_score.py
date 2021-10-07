from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import Normalizer
import joblib
import csv
import os
from reader import read_constant
from ml_tool import my_FMRegression, my_SVC


class apkToCsv():
    def __init__(self):
        self.permission = []
        self.path = ''
        self.featurePath = ''
        self.count = 0
        self.header = ['com.android.voicemail.permission.ADD_VOICEMAIL',
                       'android.permission.USE_SIP',
                       'android.permission.BIND_DEVICE_ADMIN',
                       'android.permission.READ_SYNC_SETTINGS',
                       'android.permission.READ_CALENDAR',
                       'android.permission.CHANGE_CONFIGURATION',
                       'android.permission.GET_PACKAGE_SIZE',
                       'android.permission.ACCESS_LOCATION_EXTRA_COMMANDS',
                       'android.permission.CLEAR_APP_CACHE',
                       'android.permission.BIND_INPUT_METHOD',
                       'android.permission.BIND_REMOTEVIEWS',
                       'android.permission.BATTERY_STATS',
                       'android.permission.AUTHENTICATE_ACCOUNTS',
                       'android.permission.RESTART_PACKAGES',
                       'android.permission.INTERNET',
                       'android.permission.RECORD_AUDIO',
                       'android.permission.ACCESS_MOCK_LOCATION',
                       'android.permission.WRITE_PROFILE',
                       'android.permission.READ_SOCIAL_STREAM',
                       'android.permission.VIBRATE',
                       'android.permission.WRITE_CALL_LOG',
                       'android.permission.FLASHLIGHT',
                       'android.permission.GLOBAL_SEARCH',
                       'android.permission.CHANGE_WIFI_STATE',
                       'android.permission.BROADCAST_STICKY',
                       'android.permission.KILL_BACKGROUND_PROCESSES',
                       'android.permission.SET_TIME_ZONE',
                       'android.permission.BLUETOOTH_ADMIN',
                       'android.permission.CAMERA',
                       'android.permission.SET_WALLPAPER',
                       'android.permission.WAKE_LOCK',
                       'android.permission.MANAGE_ACCOUNTS',
                       'android.permission.WRITE_CALENDAR',
                       'android.permission.SET_PREFERRED_APPLICATIONS',
                       'android.permission.NFC',
                       'android.permission.CALL_PHONE',
                       'android.permission.DISABLE_KEYGUARD',
                       'android.permission.BIND_VPN_SERVICE',
                       'com.android.browser.permission.READ_HISTORY_BOOKMARKS',
                       'android.permission.READ_SMS',
                       'android.permission.REORDER_TASKS',
                       'android.permission.MODIFY_AUDIO_SETTINGS',
                       'android.permission.READ_PHONE_STATE',
                       'android.permission.ADD_SYSTEM_SERVICE',
                       'android.permission.WRITE_SETTINGS',
                       'android.permission.BIND_WALLPAPER',
                       'android.permission.WRITE_SOCIAL_STREAM',
                       'android.permission.USE_CREDENTIALS',
                       'android.permission.SEND_SMS',
                       'android.permission.WRITE_USER_DICTIONARY',
                       'android.permission.WRITE_OWNER_DATA',
                       'android.permission.ACCESS_COARSE_LOCATION',
                       'android.permission.SET_PROCESS_FOREGROUND',
                       'android.permission.READ_EXTERNAL_STORAGE',
                       'android.permission.SYSTEM_ALERT_WINDOW',
                       'android.permission.CHANGE_WIFI_MULTICAST_STATE',
                       'android.permission.RECEIVE_BOOT_COMPLETED',
                       'com.android.alarm.permission.SET_ALARM',
                       'android.permission.WRITE_CONTACTS',
                       'android.permission.PROCESS_OUTGOING_CALLS',
                       'android.permission.EXPAND_STATUS_BAR',
                       'android.permission.READ_OWNER_DATA',
                       'android.permission.RECEIVE_MMS',
                       'android.permission.GET_TASKS',
                       'android.permission.READ_CALL_LOG',
                       'android.permission.READ_SYNC_STATS',
                       'android.permission.BIND_TEXT_SERVICE',
                       'android.permission.RECEIVE_WAP_PUSH',
                       'android.permission.SUBSCRIBED_FEEDS_WRITE',
                       'android.permission.ACCESS_WIFI_STATE',
                       'android.permission.ACCESS_FINE_LOCATION',
                       'android.permission.SUBSCRIBED_FEEDS_READ',
                       'android.permission.ACCESS_NETWORK_STATE',
                       'android.permission.FOTA_UPDATE',
                       'android.permission.WRITE_SMS',
                       'android.permission.PERSISTENT_ACTIVITY',
                       'com.android.browser.permission.WRITE_HISTORY_BOOKMARKS',
                       'android.permission.CHANGE_NETWORK_STATE',
                       'android.permission.WRITE_SYNC_SETTINGS',
                       'android.permission.BIND_ACCESSIBILITY_SERVICE',
                       'android.permission.GET_ACCOUNTS',
                       'android.permission.READ_PROFILE',
                       'android.permission.RECEIVE_SMS',
                       'android.permission.WRITE_EXTERNAL_STORAGE',
                       'android.permission.BLUETOOTH',
                       'android.permission.SET_WALLPAPER_HINTS',
                       'android.permission.READ_CONTACTS',
                       'android.permission.READ_USER_DICTIONARY',
                       'class']
        self.init = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0]

    def get_permission(self, path):
        self.path = path
        app = apk.APK(path)
        self.permission = app.get_permissions()
        # print (self.permission)

    def toCsv(self):
        self.init = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0]
        for item in self.permission:
            for index in range(len(self.header)):
                if item == self.header[index]:
                    self.init[index] = 1
        # print(self.init)
        self.featurePath = self.path + '.csv'
        test = pd.DataFrame(columns=self.header, data=[self.init])
        test.to_csv(self.featurePath, index=False)

    def score(self, model_path):
        rawdata = pd.read_csv(self.featurePath)
        T = rawdata.iloc[:, 0:88]
        testdata = np.array(T)

        clf = joblib.load(model_path)
        return 100 * clf.predict_proba(testdata)


def ml_score(apk_path):
    """
    input : apk_path
    return : a score between 0 and 100
    """
    test = apkToCsv()
    test.get_permission(apk_path)
    test.toCsv()
    return test.score(read_constant()['ml_model_path'])[0][0]
    # try:
    #     test = apkToCsv()
    #     test.get_permission(apk_path)
    #     test.toCsv()
    #     return test.score(read_constant()['ml_model_path'])
    # except Exception:
    #     raise('Fail to score.')


if __name__ == '__main__':
    apk_dir = '/home/ugstudent1/Dataset/156/malware_detection/code/data/apk/goodware/'
    apk_path = 'xyz.studiox.pixels.apk'
    # apk_path = 'zok.android.numbers.apk'
    # apk_path = 'za.co.prosense.impression.apk'
    print(ml_score(apk_dir + apk_path))