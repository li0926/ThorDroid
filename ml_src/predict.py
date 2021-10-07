import argparse
from APK import APK
import os
import sys
from extract_feature import predict_extract_feature
from two_mapping_to_identifier import predict_mapping_to_identifier
from my_generator import get_predict
from gensim.models import Word2Vec
from reader import read_constant, read_dict
from keras.models import load_model
from tools import res
import json
from extract_feature import ListFile
import random


def ParseArgs():
    Args = argparse.ArgumentParser("ThorDroid")
    Args.add_argument("--PredictDir", default='../data/predict')
    Args.add_argument("--PredictFeatureDir", default='../data/predict')
    return Args.parse_args()


def main(Args):
    os.chdir(sys.path[0])
    globals = read_constant()
    apk = APK()
    ApkDir = os.path.abspath(Args.PredictDir)
    FeatureDir = os.path.abspath(Args.PredictFeatureDir)
    Dir = dict()
    Dir[ApkDir] = FeatureDir
    #  提取目标apk特征
    predict_extract_feature(Dir, apk)
    if apk.Status != "unanalyzed":
        # 标识为映射符
        dic = read_dict(globals['mapping_to_identifier_path'])
        predict_mapping_to_identifier(FeatureDir, dic, globals['L'])
        # 加载Word2Vec模型
        model = Word2Vec.load(globals['word2vec_model_path'])
        pre = get_predict(FeatureDir, model, globals['L'], globals['K'])
        # 加载深度学习模型
        deep_model = load_model(globals['save_model_path'])
        # 修改了这里
        y_pred = deep_model.predict(pre)
        apk.API_score = int(res(y_pred[0][0]) * 100)

        if os.sep == "/":  # Linux系统
            from ml_score import ml_score
            apk.permission_score = int(ml_score(ListFile(Args.PredictFeatureDir, '.apk')[0]))
        else:
            apk.permission_score = random.randint(0, 100)  # windows系统无法安装fastFm,为测试使用,给权限值赋值随机
        # 保存
        json_apk = json.dumps(apk.todict(), ensure_ascii=False)
        print(json_apk)
    else:
        pass


if __name__ == '__main__':
    main(ParseArgs())
