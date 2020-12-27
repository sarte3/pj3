import pandas as pd
# 과제
#1) 아이티 지진시 휴대폰으로 응급사항등에 대한 전화내역 파일인
# h.csv를 읽어 데이터프레임생성,자료의 행과 열확인,자료형 확인
data = pd.read_csv('data/h.csv')
print(data)
print(data.shape)
print(type(data))

# 2)메시지종류(CATEGORY)컬럼 10줄 확인
# print(data.columns)
print(data['CATEGORY'].head(10))

# 3)CATEGORY가 널인 자료 제거,자료의 행과 열확인
data = data[pd.notnull(data['CATEGORY'])]
# print(data)
print(data.shape)

# 4)위치정보가 잘못된 자료 제거,자료의 행과 열확인
# 유효한 위치 : 18<LATITUDE<20, -75<LONGITUDE<-70
#    (18보다크고) & (20보다 작다) 
data = data[(((data['LATITUDE']>18)&(data['LATITUDE']<20))&((data['LONGITUDE']>-75)&(data['LONGITUDE']<-70)))]
print(data)
print(data.shape)