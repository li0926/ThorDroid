from extract_feature import ListFile
from multiprocessing import Process
from androguard.misc import AnalyzeAPK
import shutil


class ProcessOfFeature(Process):
    def __init__(self, processId, name, ApkFileList,MovePosition):
        super(Process, self).__init__()
        self.processId = processId
        self.name = name
        self.ApkFileList = ApkFileList
        self.MovePosition = MovePosition

    def run(self):
        ApkFileList = self.ApkFileList
        MovePosition = self.MovePosition
        for ApkFile in ApkFileList:
            # 将提取的apk文件的特征放入后缀名为.feature的文件中
            try:
                a, d, dx = AnalyzeAPK(ApkFile)
            except:
                shutil.move(ApkFile, MovePosition)
            if list(dx.get_classes()) == []:
                shutil.move(ApkFile, MovePosition)


def clean(path,MovePosition,process_number=4):
    ApkFileList = []
    ApkFileList.extend(ListFile(path, ""))
    ApkFileList.extend(ListFile(path, ".apk"))
    file_number = len(ApkFileList)
    split_ = int(file_number / process_number)
    Processes = []
    # 将要提取特征的APK文件进行划分/创建线程
    for i in range(process_number):
        if i != process_number - 1:
            process_ApkFile = ApkFileList[i * split_:(i + 1) * split_]
        else:
            process_ApkFile = ApkFileList[i * split_:]
        Processes.append(ProcessOfFeature(i + 1, "Process-" + str(i), process_ApkFile,MovePosition))
    for i in range(process_number):
        Processes[i].start()
    for t in Processes:
        t.join()


if __name__ == '__main__':
    clean('/home/ugstudent1/Dataset/156/class_malware_detection/code/data/apk/malware','/home/ugstudent1/Dataset/156/Dataset/AnalyzeFault/malware')
    print('malware completed!')
    clean('/home/ugstudent1/Dataset/156/class_malware_detection/code/data/apk/goodware','/home/ugstudent1/Dataset/156/Dataset/AnalyzeFault/goodware')
    print('goodware completed!')