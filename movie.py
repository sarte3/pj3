import pandas as pd
import matplotlib.pyplot as plt

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='D2Coding-Ver1.3.2-20180524-all.ttc').get_name()
rc('font', family=fontname)

# movies = pd.read_csv('data/ml-1m/movies.dat', sep='::', names=['MovieID', 'Title', 'Genres'])
# # print(movies)

# ratings = pd.read_csv('data/ml-1m/ratings.dat', sep='::', names=['UserID', 'MovieID', 'Rating', 'Timestamp'])
# # print(ratings)

# users = pd.read_csv('data/ml-1m/users.dat', sep='::', names=['UserID', 'Gender', 'Age', 'Occupation', 'Zip-code'])
# # print(users)

# mr = pd.merge(movies, ratings, on='MovieID')
# print(mr)
# data = pd.merge(mr, users, on='UserID')
# print(data)
# data.to_csv('data/movie2.csv', index=False)

data = pd.read_csv('data/movie2.csv')
# print(data)
# print(data.columns)

# 영화 제목 별 평점 건수
titlecnt = data.groupby('Title')['Rating'].size()
# print(titlecnt)

# 평점 정보가 200건 이상 있는 영화
r200 = titlecnt[titlecnt>=200]
# print(r200)
print(r200.index) # 평점 정보가 200건 이상 있는 영화 제목

# tips 데이터에서 토, 일 데이터만 추출
print('-'*30)
import seaborn as sns
tips = sns.load_dataset('tips')
# print(tips)

tips = tips.set_index('day')
print(tips)

print(tips.loc[['Sun', 'Sat']])