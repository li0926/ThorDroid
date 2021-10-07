


from scipy import sparse
from fastFM import als
from sklearn.svm import SVC
import numpy as np
class my_FMRegression:

    def __init__(self, n_iter=100, init_stdev=0.1, rank=8, random_state=123,
                 l2_reg_w=0.1, l2_reg_V=0.1, l2_reg=0):
        self.classifier = als.FMRegression(n_iter=1000, init_stdev=0.1, rank=2, l2_reg_w=0.1, l2_reg_V=0.5)

    def fit(self, X, y):
        return als.FMRegression.fit(self.classifier, sparse.csr_matrix(np.array(X)), np.array(y))

    def predict(self, X):
        return np.array([float(abs(i - 0) > abs(i - 1)) for i in
                         als.FMRegression.predict(self.classifier, sparse.csr_matrix(np.array(X)))])

    def get_params(self, deep=True):
        return self.classifier.get_params(deep)

    def score(self, X, y, sample_weight=None):
        return self.classifier.score(X, y, sample_weight)

    def set_params(self, params):
        return self.classifier.set_params(params)

    def predict_proba(self, X):
        res = [0] * 2
        res[int(self.predict(X))] = 1.
        return res


class my_SVC:
    def __init__(self, C=1, kernel='rbf', decision_function_shape='ovr', class_weight='balanced'):
        self.classifier = SVC(C=1, kernel='rbf', decision_function_shape='ovr', class_weight='balanced')

    def fit(self, X, y):
        return self.classifier.fit(X, y)

    def predict(self, X):
        return self.classifier.predict(X)

    def get_params(self, deep=True):
        return self.classifier.get_params(deep)

    def score(self, X, y, sample_weight=None):
        return self.classifier.score(X, y, sample_weight)

    def set_params(self, params):
        return self.classifier.set_params(params)

    def predict_proba(self, X):
        res = [0] * 2
        res[int(self.predict(X))] = 1.
        return res
