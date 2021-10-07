import argparse
import os
from extract_feature import process_extract_feature
from reader import read_constant
from tools import folders_set


def main(Args):
    # 将路径都转换为绝对路径
    MalDir = os.path.abspath(Args.MalDir)
    GoodDir = os.path.abspath(Args.GoodDir)
    GoodFeatureDir = os.path.abspath(Args.GoodFeatureDir)
    MalFeatureDir = os.path.abspath(Args.MalFeatureDir)
    Dir = dict()
    Dir[MalDir] = MalFeatureDir
    Dir[GoodDir] = GoodFeatureDir
    process_extract_feature(Dir)  # 将文件目录和特征目录形成一个字典,键是文件目录,值是特征目录


def ParseArgs(TYPE_list,apk_path,apis_path):  # 运行时添加的参数
    '''
        这里未来可能会改,现在先设定为二分类
    '''
    Args = argparse.ArgumentParser("ThorDroid")
    Args.add_argument("--MalDir", default=apk_path + '/' + TYPE_list[1])  # 训练数据的恶意样本位置
    Args.add_argument("--GoodDir", default=apk_path + '/' + TYPE_list[0])  # 训练数据的良性样本位置
    Args.add_argument("--GoodFeatureDir", default=apis_path + '/' + TYPE_list[0])
    Args.add_argument("--MalFeatureDir", default=apis_path + '/' + TYPE_list[1])
    return Args.parse_args()


def get_api(TYPE_list,apk_path,apis_path):
    main(ParseArgs(TYPE_list,apk_path,apis_path))
    print("Having finished first step:get apis!")
    return


if __name__ == "__main__":

    folders_set()
    data = read_constant()
    get_api(data['TYPE_list'],data['apk_path'],data['apis_path'])
