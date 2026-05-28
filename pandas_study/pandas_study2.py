import pandas as pd

#fruit,sale,price
df= pd.read_csv('pandas_fruit.csv')
print(df)

print(df.head(3))
print("데이터 구조", df.info())
print("데이터 정보")
print(df.describe())

print("어떤과일이 있나?")
print(df['fruit'])
print("사과만 출력")
print( df[df['fruit'] == '사과'] )

print("바나나만 출력")
print(df[df['fruit']=='바나나'] )

print("판매 수량이 10개 이상 찾기")
print(df[df['sale']>=10] )

print("판매 수량이 10개 이상이고 금액이 8만원 이상 찾기")
print(
    df[
         (df['sale']>=10)
         & (df['price']>= 80000)
    ]
)

print(" 과일 이름에 박이 포함된거 찾기")
print(
    df[
        df['fruit']
            .str
                .contains("박")
    ]
)

print("가격 높은 순으로 정렬")
print(
    df.sort_values('price',ascending=False)
)
print(
    df.sort_values(by=['fruit','sale'],ascending=False)
)

print(" 집계 함수 사용해보기")

print("과일별 판매량 합계")
print(
    df.groupby('fruit')['sale'].sum()
)

#문제 1 과일별 평균 판매 금액
print(
    df.groupby('fruit')['price'].mean().round(2)
)

print(" 판매량의 총합과 평균, 금액의 최대, 최소 구하기")
print(
    df.groupby('fruit').agg({
        'sale':['sum','mean'],
        'price':['max','min']
    })
)

print("과일 개당 가격은?")
df['un_price'] = df['price']/df['sale']
print(df)

print( "각 과일들 몇번 기록 되었나?")
print(
    df['fruit'].value_counts()
)

import matplotlib.pyplot as plt

#문제2 과일별 판매량을 그래프로 그리시오.
result = df.groupby('fruit')['sale'].sum()

result.plot(kind='bar')
plt.show()

#Ai를 통해 객체를 찾아내고 찾은 결과들을 저장해야되고
#데이터 비교, 통계, 보고서를 만들어야한다.
# 저장, 비교, 통계, 보고서
#에 numpy, matplotlib, pandas를 쓴다.

print(df)

#csv 파일 저장
df.to_csv('pandas_study\pandas_study2.csv', index=False, encoding='utf-8')