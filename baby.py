import pandas as pd
import matplotlib.pyplot as plt

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='D2Coding-Ver1.3.2-20180524-all.ttc').get_name()
rc('font', family=fontname)

# d1880 = pd.read_csv('data/baby/yob1880.txt', names=['name', 'sex', 'births'])
# print(d1880)

temp = []
for year in range(1880, 2011):
    filename = 'data/baby/yob'+str(year)+'.txt'
    # print(filename)
    d1 = pd.read_csv(filename, names=['name', 'sex', 'births'])
    # print(d1)
    d1['year'] = year
    temp.append(d1)

data=pd.concat(temp, ignore_index=True)
# print(data)

# 연도와 성별에 따른 신생아 수
s1 = data.groupby(['year', 'sex'])['births'].sum()
print(s1)