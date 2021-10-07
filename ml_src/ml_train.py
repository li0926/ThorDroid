import csv
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from scipy import sparse
from ml_tool import my_FMRegression, my_SVC

from reader import read_constant
from combo.models.classifier_comb import SimpleClassifierAggregator
from combo.utils.data import evaluate_print
from joblib import dump

import warnings

constant = read_constant()
warnings.filterwarnings("ignore")
random_state = 42

data = []
traffic_feature = []
traffic_target = []
testt_feature = []
testt_target = []
csv_file = csv.reader(open(constant['permission_train_path']))  # 样本：（训练集&验证集）
privilegenum = 88
for content in csv_file:
    content = list(map(float, content))
    if len(content) != 0:
        data.append(content)
        traffic_feature.append(content[0:privilegenum])
        traffic_target.append(content[-1])

X_train, X_test, y_train, y_test = train_test_split(traffic_feature, traffic_target, test_size=0.3)

# def fit(self, X_train, y_train, n_more_iter=0):
#     X_train = sparse.csr_matrix(X_train)
#     check_consistent_length(X_train, y_train)
#     y_train = check_array(y_train, ensure_2d=False, dtype=np.float64)
#
#     X_train = check_array(X_train, accept_sparse="csc", dtype=np.float64,
#                             order="F")
#     self.n_iter = self.n_iter + n_more_iter
#
#     if n_more_iter > 0:
#         _check_warm_start(self, X_train)
#         self.warm_start = True
#
#     self.w0_, self.w_, self.V_ = ffm.ffm_als_fit(self, X_train, y_train)
#
#     if self.iter_count != 0:
#         self.iter_count = self.iter_count + n_more_iter
#     else:
#         self.iter_count = self.n_iter
#
#     # reset to default setting
#     self.warm_start = False
#     return self


fm_classifier = my_FMRegression(n_iter=1000, init_stdev=0.1, rank=2, l2_reg_w=0.1, l2_reg_V=0.5)
svc_classifier = my_SVC(C=1, kernel='rbf', decision_function_shape='ovr', class_weight='balanced')
# fm_classifier.fit = fm_fit # lambda X_train, y_train:als.FMRegression.fit(fm_classifier, sparse.csr_matrix(np.array(X_train)), np.array(y_train))
# fm_classifier.predict = fm_predict
# fm_classifier.fit(X_train, y_train)
# print(fm_classifier.predict(X_test))
#
# t = DecisionTreeClassifier()
# t.fit(X_train, y_train)
# print(t.predict(X_test))
# fm_classifier.fit(sparse.csr_matrix(np.array(X_train)), np.array(y_train))
# fm_classifier = my_FMRegression(n_iter=1000, init_stdev=0.1, rank=2, l2_reg_w=0.1, l2_reg_V=0.5)
# fm_classifier.t_fit = fm_classifier.fit
# def fit(self, X_train, y_train_, n_more_iter=0):
#     return als.FMRegression.fit(self, sparse.csr_matrix(X_train), y_train_)
# fm_classifier.fit = fit
# fm_classifier.fit = lambda self, x, y: t_fit(self, sparse.csr_matrix(x), y)
# fm_classifier.predict = lambda self, x: self.predict(sparse.csr_matrix(x))


classifiers = [DecisionTreeClassifier(), LogisticRegression(),
               KNeighborsClassifier(), RandomForestClassifier(n_estimators=36),
               GradientBoostingClassifier(),
               svc_classifier, fm_classifier]

clf_weights = np.array([0.025, 0.025, 0.025, 0.85, 0.025, 0.025, 0.025])
clf = SimpleClassifierAggregator(classifiers, method='majority_vote',
                                 weights=clf_weights)
clf.fit(X_train, y_train)
dump(clf, constant['ml_model_path'])
y_test_predicted = clf.predict(X_test)
evaluate_print('Combination by w_vote|', y_test, y_test_predicted)
