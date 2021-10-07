from reader import read_constant
from scipy import sparse
from sklearn.svm import SVC
import numpy as np
import os




def mkdir(path):  # 创建文件夹
    import os
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径


def folders_set():
    globals = read_constant()
    mkdir(globals['identifiers_path'])
    for i in range(globals['TYPE']):
        mkdir(globals['apis_path'] + '/' + globals['TYPE_list'][i])
        mkdir(globals['train_path'] + '/' + globals['TYPE_list'][i])
        mkdir(globals['test_path'] + '/' + globals['TYPE_list'][i])
    return True


def res(x):
    return (2 * x - 1) ** 5 / 2 + 0.5


def JudgeLinux():
    """
    :return: 判断当前操作系统是否为Linux
    """
    return os.sep == "/"


# class my_FMRegression:
#     from fastFM import als
#
#     def __init__(self, n_iter=100, init_stdev=0.1, rank=8, random_state=123,
#                  l2_reg_w=0.1, l2_reg_V=0.1, l2_reg=0):
#         self.classifier = als.FMRegression(n_iter=1000, init_stdev=0.1, rank=2, l2_reg_w=0.1, l2_reg_V=0.5)
#
#     def fit(self, X, y):
#         return als.FMRegression.fit(self.classifier, sparse.csr_matrix(np.array(X)), np.array(y))
#
#     def predict(self, X):
#         return np.array([float(abs(i - 0) > abs(i - 1)) for i in
#                          als.FMRegression.predict(self.classifier, sparse.csr_matrix(np.array(X)))])
#
#     def get_params(self, deep=True):
#         return self.classifier.get_params(deep)
#
#     def score(self, X, y, sample_weight=None):
#         return self.classifier.score(X, y, sample_weight)
#
#     def set_params(self, params):
#         return self.classifier.set_params(params)
#
#     def predict_proba(self, X):
#         res = [0] * 2
#         res[int(self.predict(X))] = 1.
#         return res
#
#
# class my_SVC:
#     def __init__(self, C=1, kernel='rbf', decision_function_shape='ovr', class_weight='balanced'):
#         self.classifier = SVC(C=1, kernel='rbf', decision_function_shape='ovr', class_weight='balanced')
#
#     def fit(self, X, y):
#         return self.classifier.fit(X, y)
#
#     def predict(self, X):
#         return self.classifier.predict(X)
#
#     def get_params(self, deep=True):
#         return self.classifier.get_params(deep)
#
#     def score(self, X, y, sample_weight=None):
#         return self.classifier.score(X, y, sample_weight)
#
#     def set_params(self, params):
#         return self.classifier.set_params(params)
#
#     def predict_proba(self, X):
#         res = [0] * 2
#         res[int(self.predict(X))] = 1.
#         return res
