import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='D2Coding-Ver1.3.2-20180524-all.ttc').get_name()
rc('font', family=fontname)

# c1 = pd.read_csv('data/concat_1.csv')
# # print(c1)
# c2 = pd.read_csv('data/concat_2.csv')
# # print(c2)
# c3 = pd.read_csv('data/concat_3.csv')
# c3['zz']='zz'
# # print(c3)

# d1 = pd.concat([c1, c2, c3], ignore_index=True)
# print(d1)
# d2 = pd.concat([c1, c2, c3], ignore_index=True, join='inner')
# print(d2)
# d3 = pd.concat([c1, c2, c3], axis=1, ignore_index=True)
# print(d3)

person = pd.read_csv('data/survey_person.csv')
print(person)
survey = pd.read_csv('data/survey_survey.csv')
print(survey)
# merge() : 2개의 데이터프레임 기준에 의해 연결
ps = pd.merge(person, survey, left_on='ident', right_on='person')
print(ps)
visited = pd.read_csv('data/survey_visited.csv')
print(visited)
psv = ps.merge(visited, left_on='taken', right_on='ident')
print(psv)
# site = pd.read_csv('data/survey_site.csv')
# print(site)
