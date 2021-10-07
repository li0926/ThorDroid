import os
import random
from reader import read_constant, read_dict, Get_file_line
import multiprocessing
from tools import folders_set
from extract_feature import ListFile


def predict_mapping_to_identifier(Path,dic,L):  # 单个ApkFeature文件路径
    ApkFeatureFile = []
    ApkFeatureFile.extend(ListFile(Path, ".feature"))

    for FeatureFile in ApkFeatureFile:
        f = Get_file_line(FeatureFile)
        lens = len(f)
        g = []
        for k in f:
            m = k[:-1]
            if m in dic.keys():  # 当长度小于L时后面补0；当api不在dict关键字里面，map到0
                identifier = str(dic[m]) + '\n'
            else:
                identifier = '0\n'
            g.append(identifier)
        pos = FeatureFile.index('.')
        ApkName = FeatureFile[:pos]
        fp = open(ApkName+'.identifier','w')
        fp.writelines(g)
        fp.close()
        # with open(Path + '/' + ApkName + '.identifier','w') as x:
        #     x.writelines(g)



def mapping_to_identifier(TYPE, TYPE_list, dic, L, apis_path, train_path, test_path, val_split):
    for i in range(TYPE):
        files = os.listdir(apis_path + '/' + TYPE_list[i])
        number = len(files)
        test_number = int(number * val_split)
        train_number = number - test_number
        random.shuffle(files)
        for j in range(number):
            f = Get_file_line(apis_path + '/' + TYPE_list[i] + '/' + files[j])
            lens = len(f)
            g = []
            for k in range(L):  # 限制sentence长为L
                if (k < lens) and (f[k][:-1] in dic.keys()):  # 当长度小于L时后面补0；当api不在dict关键字里面，map到0
                    m = f[k][:-1]
                    g.append(str(dic[m]) + '\n')
                else:
                    g.append('0\n')
            if j < train_number:
                with open(train_path + '/' + TYPE_list[i] + '/' + files[j], 'w') as x:
                    x.writelines(g)
            else:
                with open(test_path + '/' + TYPE_list[i] + '/' + files[j], 'w') as x:
                    x.writelines(g)
    print("Having finished second step:mapping to idnetifier!")
    return


def fun(id, val_split, apis_path, TYPE_list, dic, files, train_path, test_path):
    num = len(files)
    test_number = int(num * val_split)
    train_number = num - test_number

    for j in range(num):
        f = Get_file_line(apis_path + '/' + TYPE_list + '/' + files[j])
        lens = len(f)
        if lens == 0:
            continue
        g = []
        for k in f:  # 限制sentence长为L
            m = k[:-1]
            if m in dic.keys():  # 当长度小于L时后面补0；当api不在dict关键字里面，map到0
                identifier = str(dic[m]) + '\n'
            else:
                identifier = '0\n'
            g.append(identifier)
        if j < train_number:  # 分为数据集和训练集
            with open(train_path + '/' + TYPE_list + '/' + files[j], 'w') as x:
                x.writelines(g)
        else:
            with open(test_path + '/' + TYPE_list + '/' + files[j], 'w') as x:
                x.writelines(g)


def process_mapping_to_identifier(TYPE, TYPE_list, dic, apis_path, train_path, test_path, val_split, process_number=4):
    for i in range(TYPE):
        print(apis_path + '/' + TYPE_list[i])
        files = os.listdir(apis_path + '/' + TYPE_list[i])
        split_ = int(len(files) / process_number)
        random.shuffle(files)
        Processes = []
        for j in range(process_number):
            if j != process_number - 1:
                process_ApkFile = files[j * split_:(j + 1) * split_]
            else:
                process_ApkFile = files[j * split_:]
            p = multiprocessing.Process(target=fun, args=(
                j, val_split, apis_path, TYPE_list[i], dic, process_ApkFile, train_path, test_path))
            p.start()
            Processes.append(p)
        for pro in Processes:
            pro.join()


if __name__ == "__main__":
    folders_set()
    data = read_constant()
    dic = read_dict(data['mapping_to_identifier_path'])
    process_mapping_to_identifier(data['TYPE'], data['TYPE_list'], dic, data['apis_path'], data['train_path'],
                                  data['test_path'], data['val_split'])
