#pandas 는 데이터 분석용 라이브러리
#numpy 는 숫자배열 계산
#pandas 는 데이터를 '표'형식으로 관리하여 분석용이
#numpy[ [1,2] , [3,4] ]
#pandas
#이름 점수
#이순신 89
#박운수 67
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.DataFrame( # 2차원 표 데이터
    {
        "name":["이순신","박문수","홍길동","전우치","페이커","박지성","김연아"],
        "score":[89,67,50,33,100,85,94],
        "gender":["남","남","남","남","남","남","여"]
    }
)
print(df)
print(df['name'])
print(df['score'].sum())

print("\n 데이터 프레임 -행 단위 출력하기\n")
print(df.head(3))
print(df.tail(3))
#head 와 tail 함수는 파일데이터 불러오기 했을때 확인용으로 많이 사용
#로그 파일을 확인할때 최근문제를 보려면  tail 함수로 빠르게확인가능

print("\n 데이터 프레임의 데이터 정보 확인\n")
print(df.info())
print(df.describe())
#숫자 데이터의 평균 , 최소값 , 최대값 , 분포 , 데이터 갯수 , 표준편차
print("\n 데이터 프레임 조건 검색\n")
res_df = df[df['score']>=80]
print(res_df)

name_df= df[df['name'].str.contains("이")]
print(name_df)
#문자열 완전일치는 == 연산자
res_df = df [ (df['score'] >= 80) & (df['score']<=90)]
print("== 연산자 : ",res_df)

#여러개 검색 에는 isin 함수 사용
res_df = df [ df['name'].isin(["이순신", "한석봉"])]
print(res_df)
#범위 검색 between
res_df = df[df['score'].between(80, 90)]
print("범위 검색 : ",res_df)

res_df = df.query('score >= 80 and score <= 90')
print("범위 검색 : ",res_df)

#특정 컬럼(필드)만 가져오기
res_df = df.loc[ df['score'] >= 80]
print("특정컬럼 :",res_df)

res_df = df.sort_values(by='score', ascending=False) # 오름차순 False 내림차순 Ture
print(res_df)

#특정 컬럼 안에 데이터가 몇개 있는지
print(df['score'].value_counts())

#그룹화
res_df = df.groupby('gender')['score'].sum()
print("그룹화 : ",res_df)
'''
groupby 의 집계 함수들
컬럼이 여러개라면 함수 앞에 집계할 컬럼 넣어야된다.
sum() -총합 df.groupby('gender').sum()
mean() - 평균 df.groupby('gender').mean()
count() - 개수 df.groupby('gender').count()
size() - 행 개수 df.groupby('gender').size()
    count 와 size 의 결과가 같은 경우가 많은데 
    차이는 count 는 NaN 제외하고 개수 파악, size는 NaN 포함 개수 확인
    
std() - 표준 편차 df.grouby('gender').std()
min() , max()
median() - 중앙값 df.groupby('gender').median()
var() - 분산 df.groupby('gender').var()
first() - 첫번째 값 df.groupby('gender').first()
last()

agg() - 여러개의 집계 함수 사용 df.groupby('gender').agg()(['sum','mean'])
컬럼별로 다른 집계함수 사용
 df.groupby('gender').agg({
    "score" : "sum",
    "name" : "count"
    })    
    
'''

s= pd.Series([89,67]) # 1차원 데이터
print("1차원 데이터:", s)