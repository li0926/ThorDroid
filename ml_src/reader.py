import json


def read_constant(pos='./constant.json'):
    fp = open(pos, 'r')
    data = json.load(fp)
    data['maxpooling_size'] = (data['maxpooling_size'][0], data['maxpooling_size'][1])
    data['type_map'] = {data['TYPE_list'][i]: i for i in range(data['TYPE'])}
    return data



def read_dict(path):  # 读取映射到标识符的函数
    import pickle
    dict_file = open(path, 'rb')
    dic = pickle.load(dict_file)
    return dic


def Get_file_line(filename, L=-1):  # 将文件的行组成list,L标识文件读多少行，当-1时全读,如果不够补0
    with open(filename, encoding='utf-8') as f:
        Sequence = f.readlines()
        if L != -1:
            lens = len(Sequence)
            if L <= lens:
                Sequence = Sequence[:L]
            else:
                Sequence.extend(['0\n'] * (L - lens))
    return Sequence


def sentences_append(sentences, path, L=-1):  # 将path目录下的所有文件的行放入文件，形成了二维矩阵，ij中i是文件，j是文件的行,L标识每个文件读多少行，当-1时全读
    import os
    files = os.listdir(path)
    for i in range(len(files)):
        sentences.append(Get_file_line(path + '/' + files[i], L))
    return files


def read_report(path,apk):
    with open(path,'r',encoding='utf-8') as f:
        s = json.load(f)
        apk.TelephonyIdentifiersLeakage = s[1]['analysis_results'][0][1]
        if len(s[1]['analysis_results'][1][1])>=100:
            apk.DeviceSettingsHarvesting = s[1]['analysis_results'][1][1][:100]
        else:
            apk.DeviceSettingsHarvesting = s[1]['analysis_results'][1][1]
        apk.LocationLookup = s[1]['analysis_results'][2][1]
        apk.ConnectionInterfacesExfiltration = s[1]['analysis_results'][3][1]
        apk.TelephonyServicesAbuse = s[1]['analysis_results'][4][1]
        apk.AudioVideoEavesdropping = s[1]['analysis_results'][5][1]
        apk.SuspiciousConnectionEstablishment = s[1]['analysis_results'][6][1]
        apk.PimDataLeakage = s[1]['analysis_results'][7][1]
        apk.CodeExecution = s[1]['analysis_results'][8][1]



if __name__ == '__main__':
    read_dict()
