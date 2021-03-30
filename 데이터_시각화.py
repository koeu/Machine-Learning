%matplotlib inline

import pandas as pd
import numpy as np

df = pd.read_csv('./broadcast.csv', index_col = 0)
df.plot()
df.plot(kind = 'line')
df.plot(y ='KBS')
df.plot(y =['KBS', 'JTBC'])
df[['KBS', 'JTBC']]
df['KBS'].plot()

## 막대그래프 - 카데고리 비교를 위해 사용
df = pd.read_csv('./sports.csv', index_col = 0)
df.plot(kind = 'bar')
df.plot(kind = 'barh')
df.plot(kind = 'bar', stacked = True)

# 여성을 대상으로 한 스포츠 선호도 조사 그래프 그리기
df['Female']
df['Female'].plot(kind = 'bar')

# 파이 그래프 - 절대적인 수치보다 비율
df = pd.read_csv('./broadcast.csv', index_col = 0)
df.loc[2017]
df.loc[2017].plot(kind = 'pie')

# 히스토그램 - 범위로 묶어서
df = pd.read_csv('./body.csv', index_col = 0)
df.plot(kind = 'hist', y = 'Height')
df.plot(kind = 'hist', y = 'Height', bins = 15)
# 상세하다고 좋은건 아님

df.plot(kind = 'hist', y = 'Height', bins = 200)
# 상황에 맞는 적당한 bin 수 선택해야 함
