import pandas as pd

# titanic 파일 
TITANIC_FILE_PATH = './titanic.csv'
titanic_df = pd.read_csv(TITANIC_FILE_PATH)
titanic_df.head()

titanic_sex_embarked = titanic_df[['Sex', 'Embarked']]
titanic_sex_embarked.head()

one_hot_encoded_df = pd.get_dummies(titanic_sex_embarked)
one_hot_encoded_df.head()

# 원하는 두 열만 one-hot-encoding 하기
one_hot_encoded_df = pd.get_dummies(data = titanic_df, columns = ['Sex', 'Embarked'])
one_hot_encoded_df.head()
