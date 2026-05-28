import numpy as np

#2차원 배열
#[ [1,2,3]. [4,5,6] ]

arr = np.array((
    (1,2,3),
    (4,5,6)
)) #numpy 2차원 배열은 2차원 리스트를 통해 만든다.
print(arr)
arr[0][0]= 100
print(arr.shape) # (2,3) " 2행 3열의 2차원 배열

print( arr[1][0])
print( arr[1]) #행 전체
print( arr[:, 1]) #모든행에서 2열값 가져오기 , 두번째 열만 나옴
print( arr[0,1]) # arr[0][1]
arr[0][1] =400
print(arr)
arr[0,1]= 500
print(arr)
print(arr[1]+100)
#배열 정보 확인
#arr .dtype: 데이터타입
#arr . size: 총 데이터 개수
#arr .shape: 배열의 모양 (차원과 갯수)
#arr . ndim: 배열의 차원수

#문제 1
scores = np.array([
    [98,89,78],
    [94,74,56],
    [75,68,81]
])
#scores은 몇차원이고 총 데이터 갯수는?
#2행의 총합은?
#3열 전체를 출력하시오
#scores 전체의 평균값은?
#2열의 평균은?

print(scores.ndim , "차원 배열 ," , "총 데이터 갯수 : ",scores.size)

print(scores[1].sum())
print(scores[:, 2])
print(scores.mean())
print(scores[:, 1].mean())