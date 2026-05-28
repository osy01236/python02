import numpy as np
#배열에서 원하는 위치 데이터 가져오기
arr = np.random.randint(0,50,12)
print(arr)

#슬라이싱
print( arr[3:8])
print( arr[:4]) # : 4 - > 0번인덱스부터 3번까지
                # : 2: -> 2번인덱스부터 끝까지
print(arr[::2]) # ::2 ->2칸씩
print(arr[::-1]) # 역방향으로 출력

arr2= np.random.randint(0,50,(3,4))
print(arr2)
print(arr2[1])
print(arr2[:,2])
print(arr2[0:1, 1:3])

#fancy indexing : 원하는 위치만 고르기
print( arr[[0,4,7]]) # [[ 인덱스, 인덱스 ]] 원하는 인덱스 번호 넣기

print(arr2[[0,2]] ) # 2차원배열에서는 행을 선택
print(arr2[[0,2],[1,3]]) #0번인덱스의 1번, 2번 인덱스의 3번  (앞이 행, 뒤가 열)

#boolean indexing
print( arr> 30 )
print( arr[ arr>30] )
print(arr[arr% 2== 1]) ## 2로나눳을때 1이남는 홀수찾기


print(arr2[ arr2 >15 ])

#학생 5명의 6과목 성적을 배열로 저장하세요. ( 성적은 50 ~ 100 사이 임의값)
#학생 5명 성적이 저장된 배열에서 성적이 80점 이상만 출력하세요.
sunjuk = np.random.randint(50,101,(5,6))
print(sunjuk)
print( sunjuk [sunjuk >= 80])

pos= np.argwhere( sunjuk >= 80)
print(pos)

#흑백 사진에서 밝은 영역이 어디인지 찾아서 표시하시오.
#어둠 - 0 , 빛 - 255
#200 이상인 영역을 찾기
img = np.array([
    [10,20,30,40,50],
    [60,200,210,70,80],
    [90,220,255,100,110],
    [120,130,140,150,160]
])

bri = img >=200
print(bri)
#밝은 영역을 더 밝게 !
copy_img = img.copy() # 원본데이터 유지를 위한 복사
copy_img[copy_img>=200] = 255
print(copy_img)

#밝은 영역이 몇군데??
count = np.sum(copy_img==255)
print(count,"개")
#밝은 영역의 좌표는??
pos = np.argwhere( copy_img == 255)
print("좌표는?",pos)

#밝은 영역 위치 의 값만 출력하기
rows = pos[:,0]
cols = pos[:,1]

min_row = rows.min() #행번호의 최소값
max_row = rows.max()#행번호의 최대값
min_col = cols.min() #열변호의 최소값
max_col = cols.max()#열변호의 최대값
#img[1:2 , 1:2]
find = img[min_row : max_row + 1, min_col : max_col + 1]
print(find)