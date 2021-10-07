# coding=utf-8

import os
from androguard.misc import AnalyzeAPK
import json
from multiprocessing import Process
from reader import read_report
import time
from tools import JudgeLinux
import sys

from functools import reduce


def sensitive_behaviors_scores(dx):
    behaviors_class = ["class1", "class2", "class3", "class4", "class5", "class6"]
    behaviors_apis = {"class1": ['Landroid.telephony.SmsManager;sendDataMessage',
                                 'Landroid.telephony.SmsManager;sendMultipartTextMessage',
                                 'Landroid.telephony.TelephonyManager;getLine1Number',
                                 'Landroid.telephony.TelephonyManager;listen'],
                      "class2": ['Landroid.accounts.AccountManager;getAccountsByType',
                                 'Landroid.app.ActivityManager;killBackgroundPreocess'],
                      "class3": ['Ljava.net.URL;openConnetction',
                                 'Landroid.app.NotificationManager;notify',
                                 'Landroid.content.pm.PackageManager;setComponentEnabledSetting'],
                      "class4": ['Landroid.media.AudioRecord;startRecording',
                                 'Landroid.net.ConnectivityManager;setMobileDataEnable',
                                 'Landroid.media.MediaRecorder;start',
                                 'Landroid.media.MediaRecorder;stop', ],
                      "class5": ['Landroid/location/LocationManager;getLastKnownLocation',
                                 'Landroid/location/LocationManager;requestSingleUpdate',
                                 'Landroid/location/LocationManager;requestLocationUpdates'],
                      "class6": ['Ljava/lang/Runtime;exec']
                      }

    """
    class1 : 电话短信
    class2 : 收集账户信息
    class3 : 建立连接，发通知
    class4 : 音频视频
    class5 : 获取地理位置
    class6 : 命令行代码执行
    """

    behaviors_scores = {"class1": 0, "class1": 0, "class2": 0, "class3": 0, "class4": 0, "class5": 0, "class6": 0}
    sum_score = 0
    i = 0
    for behavior in behaviors_class:
        behavior_score = 0
        apis_list = behaviors_apis[behavior]
        for api in apis_list:
            behavior_score += number_of_leaf_nodes_of_call_tree(dx, api)
        behaviors_scores[behavior] = min(behavior_score,9)
        sum_score += behaviors_scores[behavior]*pow(10,i)
        i += 1
        # print("the score of behavior {:s}  is {:d}".format(behavior, behavior_score))
    return sum_score


def number_of_leaf_nodes_of_call_tree(dx, api: str):
    number = 0
    k = api.split(';')
    class_name = k[0]
    method_name = k[1]
    method_analysises = dx.find_methods(class_name, method_name)  # m为MethodAnalysis类型对象
    for method_analysis in method_analysises:
        number += deep_count(method_analysis, 0)
    # print("the number of nodes of call {:s} tree is {:d}".format(api,number) )
    return number


def deep_count(method_analysis, count: int = 0):
    paths = method_analysis.get_xref_from()
    if not paths or len(paths) == 0 or count > 20:
        return 1
    else:
        result = 0
        for c, m, _ in paths:
            result += (deep_count(m, count + 1))
        return int(result)


class ProcessOfFeature(Process):
    def __init__(self, processId, name, ApkFileList, ApkDirectoryPaths):
        super(Process, self).__init__()
        self.processId = processId
        self.name = name
        self.ApkFileList = ApkFileList
        self.ApkDirectoryPaths = ApkDirectoryPaths

    def run(self):
        ApkFileList = self.ApkFileList
        ApkDirectoryPaths = self.ApkDirectoryPaths
        for ApkFile in ApkFileList:
            # 将提取的apk文件的特征放入后缀名为.feature的文件中
            path = os.path.join(ApkDirectoryPaths[os.path.split(ApkFile)[0]], os.path.split(ApkFile)[1])

            if JudgeFileExist(path + '.feature'):
                pass
            else:
                try:
                    a, d, dx = AnalyzeAPK(ApkFile)
                except:
                    continue
                if list(dx.get_classes()) == []:
                    continue
                fp = open(path + '.feature', 'w')
                for ApkClass in dx.get_classes():
                    for meth in dx.classes[ApkClass.name].get_methods():
                        s = [(call.class_name, call.name) for _, call, _ in meth.get_xref_to()]
                        all_instructions = get_all_instructions(meth)
                        s_ = sort_s(s, all_instructions)
                        for call0, call1 in s_:
                            fp.write("{}:{}\n".format(call0, call1))
                fp.close()


def JudgeFileExist(FilePath):
    """
        给定文件路径,判断是否存在该文件
    """
    if os.path.exists(FilePath) == True:
        return True
    else:
        return False


def analyze_androwarn(path, ApkFile, apk):
    """

    :param path: 分析的ApkFile的所在目录的绝对路径
    :param ApkFile: ApkFile的位置
    :return:
    """
    if JudgeLinux():  # 使用系统为Linux,服务器内网ip:10.102.32.144
        cmd = '~/.conda/envs/ad/bin/python ' + sys.path[
            0] + '/androwarn.py -i ' + ApkFile + ' -o ' + ApkFile + ' -v 3 -r json'
    else:
        cmd = "C:\\Users\\rocku\\miniconda3\\python.exe " + sys.path[
            0] + '\\androwarn.py -i ' + ApkFile + ' -o ' + ApkFile + ' -v 3 -r json'
    os.system(cmd)
    JsonFile = ListFile(path, ".json")[0]
    read_report(JsonFile, apk)


def ListFile(FilePath, extensions):
    """
    给定文件夹的路径和要提取的文件扩展名,返回一个文件列表
    """
    Files = []
    filenames = os.listdir(FilePath)
    for file in filenames:
        AbsolutePath = os.path.abspath(os.path.join(FilePath, file))  # 文件的绝对路径
        if os.path.splitext(file)[1] == extensions:  # os.path.splitext分离文件名和扩展名
            Files.append(AbsolutePath)
    return Files


def get_all_instructions(meth):
    """

    :param meth: apk的method
    :return: 返回 method的所以指令
    """
    basic_block = meth.basic_blocks.gets()
    all_instructions = list()
    for block in basic_block:
        all_instructions.extend(block.get_instructions())
    return all_instructions


def sort_s(s, all_instrution):
    """

    :param s: 提取出来的instrcution
    :param all_instrution: 所有的instruction
    :return:
    """
    s_ = set()

    for call0, call1 in s:
        api = str(call0) + '->' + str(call1)
        s_.add(api)
    ele_list = []
    all_instrution = [str(ins) for ins in all_instrution]
    import re
    for i in all_instrution:
        t = re.split('( )|(\()', i)
        # if len(t) > 3 and t[-4] in s_:
        #     ele_list.append(tuple(t[-4].split('->')))
        for j in t:
            if j in s_:
                ele_list.append(tuple(j.split('->')))
                break
    return ele_list


def Mapping_Third(Writelines, ThirdClassDict):
    """

    :param Writelines: 将要写入的apk的method
    :param ThirdClassDict: 每一个APK对应的第三方的字典
    :return: UpDateWritelines
    """
    UpDateWriteLines = []
    for l in Writelines:
        if l.strip() in list(ThirdClassDict.keys()):
            UpDateWriteLines.extend(ThirdClassDict[l.strip()])
        else:
            UpDateWriteLines.extend([l])
    return UpDateWriteLines


def extract_feature(ApkDirectoryPaths):
    """
        将给定的恶意软件目录的apk文件和良性软件的apk文件的feature提取出来
    """
    start = time.time()

    ApkFileList = []
    for FilePath in ApkDirectoryPaths.keys():
        # 将没有后缀名的和后缀名为apk的文件添加到路径中
        ApkFileList.extend(ListFile(FilePath, ""))
        ApkFileList.extend(ListFile(FilePath, ".apk"))

    for ApkFile in ApkFileList:
        # 将提取的apk文件的特征放入后缀名为.feature的文件中
        path = os.path.join(ApkDirectoryPaths[os.path.split(ApkFile)[0]], os.path.split(ApkFile)[1])

        if JudgeFileExist(path + '.feature'):
            pass
        else:
            try:
                a, d, dx = AnalyzeAPK(ApkFile)
            except:
                continue
            if list(dx.get_classes()) == []:
                continue
            fp = open(path + '.feature', 'w')
            for ApkClass in dx.get_classes():
                for meth in dx.classes[ApkClass.name].get_methods():
                    s = [(call.class_name, call.name) for _, call, _ in meth.get_xref_to()]
                    all_instructions = get_all_instructions(meth)
                    s_ = sort_s(s, all_instructions)
                    for call0, call1 in s_:
                        fp.write("{}:{}\n".format(call0, call1))
            fp.close()
    print("time cost :", time.time() - start)
    return


def predict_extract_feature(ApkDirectoryPaths, apk):
    """
        将给定的恶意软件目录的apk文件和良性软件的apk文件的feature提取出来
    """
    with open("RiskFunctionList.json", encoding="utf-8") as f:
        RiskFuntionDict = json.load(f)
    ApkFileList = []
    for FilePath in ApkDirectoryPaths.keys():
        # 将没有后缀名的和后缀名为apk的文件添加到路径中
        ApkFileList.extend(ListFile(FilePath, ""))
        ApkFileList.extend(ListFile(FilePath, ".apk"))

    for ApkFile in ApkFileList:
        # 将提取的apk文件的特征放入后缀名为.feature的文件中
        path = os.path.join(ApkDirectoryPaths[os.path.split(ApkFile)[0]], os.path.split(ApkFile)[1])

        if JudgeFileExist(path + '.feature'):
            apk.Status = "analyzed"
            pass
        else:
            try:
                a, d, dx = AnalyzeAPK(ApkFile)
            except:
                apk.Status = "unanalyzed"
                continue
            if list(dx.get_classes()) == []:
                apk.Status = "unanalyzed"
                continue
            fp = open(path + '.feature', 'w')
            #  获取apk的权限..
            Permission = a.get_permissions()
            PackageName = a.get_package()
            Activities = a.get_activities()
            MinSdkVersion = a.get_min_sdk_version()
            RiskFunction = dict()
            ThirdClassDict = dict()
            WriteList = []
            for ApkClass in dx.get_classes():
                for meth in dx.classes[ApkClass.name].get_methods():  # 获得class的methods
                    s = [(call.class_name, call.name) for _, call, _ in meth.get_xref_to()]
                    all_instructions = get_all_instructions(meth)
                    s_ = sort_s(s, all_instructions)
                    TempMap = []
                    ThirdClassDict[ApkClass.name + ':' + meth.name] = s_  # 将第三方的方法名进行映射
                    for call0, call1 in s_:
                        TempMap.append("{}:{}\n".format(call0, call1))
                        # fp.write("{}:{}\n".format(call0,call1))
                        api = call0 + ":" + call1
                        if api in list(RiskFuntionDict.keys()):
                            RiskFunction[str(api)] = RiskFuntionDict[api]

                    WriteList.extend(TempMap)
            #         ThirdClassDict[ApkClass.name + ':' + meth.name] = TempMap  # 将第三方的方法名进行映射
            # WriteList = Mapping_Third(WriteList,ThirdClassDict)
            analyze_androwarn(os.path.split(ApkFile)[0], ApkFile, apk)
            fp.writelines(WriteList)
            fp.close()
            apk.behavior_scores = sensitive_behaviors_scores(dx)
            apk.Permission = Permission
            apk.RiskFunction = RiskFunction
            apk.PackageName = PackageName
            apk.Activities = Activities
            apk.Status = "analyzed"
            apk.MinSdkVersion = MinSdkVersion
    return


def process_extract_feature(ApkDirectoryPaths, process_number=4):  # 多进程提取特征
    start = time.time()
    ApkFileList = []
    for FilePath in ApkDirectoryPaths.keys():
        # 将没有后缀名的和后缀名为apk的文件添加到路径中
        ApkFileList.extend(ListFile(FilePath, ""))
        ApkFileList.extend(ListFile(FilePath, ".apk"))
    file_number = len(ApkFileList)
    split_ = int(file_number / process_number)
    Split_Apk_File = []
    Processes = []
    # 将要提取特征的APK文件进行划分/创建线程
    for i in range(process_number):
        if i != process_number - 1:
            process_ApkFile = ApkFileList[i * split_:(i + 1) * split_]
        else:
            process_ApkFile = ApkFileList[i * split_:]
        Processes.append(ProcessOfFeature(i + 1, "Process-" + str(i), process_ApkFile, ApkDirectoryPaths))
    # 开启线程
    for i in range(process_number):
        Processes[i].start()
    for t in Processes:
        t.join()
