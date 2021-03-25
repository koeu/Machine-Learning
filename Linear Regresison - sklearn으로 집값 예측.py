#scikit-learn
#개발자들이 만든 라이브러리

from sklearn.datasets import load_boston  #보스턴 집값 데이터셋
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
boston_dataset = load_boston()

# DESCR = description
print(boston_dataset.DESCR)

#input: 13, output: 1 (집값)

boston_dataset.feature_names
boston_dataset.data
boston_dataset.data.shape  #506개 집 데이터 with 13개 속성
boston_dataset.target  # 보스턴 집 값
boston_dataset.target.shape #차원이 506인 벡터 

x = pd.DataFrame(boston_dataset.data, columns = boston_dataset.feature_names)
#x = x[['AGE']]  # 열 하나만 가져오기
y = pd.DataFrame(boston_dataset.target, columns = ['MEDV'])
#train, 80%  test set 20% 나누기 매번 20%의 똑같은 값만 뽑아내기
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=5)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

model = LinearRegression()

# train 학습
model.fit(x_train, y_train)

#theta_!
model.coef_

#the_0
model.intercept_

# f(x) = 31.04617413 - 0.12402883x

# test set으로 모델 평가하기
y_test_prediction = model.predict(x_test)

#평균 제곱근 오차 계산 = sqrt(MSE) = RMSE
mean_squared_error(y_test, y_test_prediction) **0.5

# 8천 달러의 오차가 있음
