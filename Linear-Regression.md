Linear Regression 선형회귀
===========================
- 지도학습, 회귀
- 데이터에 적절한 하나의 선 (최적선) 찾기
- RMSE를 최소화 하는 theta 찾기

##### ** 가설함수 (Hypothesis Function) **
   y = ax + b    =>   h(x) = theta_0 + theta_1 * x   => h_theta(x) = theta_0 + theta_1 * x1 + theta_2 * x2 + ... + theta_n * xn
   
#### ** 가설함수 평가법 **
   1. 평균 제곱 오차 (Mean Squared Error: MSE)
      MSE ↑ → 평균제곱 오차 ↑ = 가설함수가 데이터에 잘 안 맞음 (Bad)
      MSE ↓ → 평균제곱 오차 ↓ = 가설함수가 데이터에 잘 맞음 (Good)
   2. 평균 제곱근 오차 (Root Mean Squared Error: RMSE)
      RMSE = root(MSE)
####
