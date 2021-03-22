from sklearn import datasets
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

import warnings
warnings.simplefilter(action='ignore', category = FutureWarning)

iris_data = datasets.load_iris()

X = pd.DataFrame(iris_data.data, columns = iris_data.feature_names)
y = pd.DataFrame(iris_data.target, columns = ['class'])

logistic_model = LogisticRegression(max_iter = 2000)

#1. 모델, 2. 입력변수, 3. 입력변수 (여기서 경고 메세지 나타내기 위해 .values.ravel() 사용, 4. cv = 몇 겹인지 정하기)
np.average(cross_val_score(logistic_model, X, y.values.ravel(), cv = 5))
# average= 평균 성능 계산
