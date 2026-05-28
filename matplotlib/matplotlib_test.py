"""
    125번 png 와 json파일을 사용하여 다음을 만들어보세요.
    이미지안에서 차량의 크기가 가장 큰 차와 크기가 세번쨰로 큰 차를 바운딩 박스로 표시해주세요.
    가장큰차의 바운딩 박스 테두리 색은 red
    세번째로 큰 차의 바운딩박스 테두리색은 yellow


"""
import matplotlib.pyplot as plt
import numpy as np
import json
import matplotlib.patches as patches
from PIL import Image

with open("18396708_frame_125.json", "r", encoding='utf-8') as f:
    data = json.load(f)

#차량 정보를 저장할 리스트( 앞에 size 부터 넣어서 크기 순서대로 들어가게끔)
vehicles=[]
#json 안에서 annotations 목록을 하나씩 꺼내서 반복
for ann in data['frames']['annotations']:
    code =ann['category']['code']  #현재 annotation의 종류를 가져옴
    if code != 'vehicle': # vehicle 가 아니면 실행 x
        continue
    label = ann['label'] # vehicle인 경우, 박스 좌표 정보가 들어있는 label을 가져옴
    x= label['x']
    y= label['y']
    width = label['width']
    height = label['height']

    size = width*height #  차량 크기
    # 차량 정보를 리스트에 저장
    vehicles.append([size,x,y,width,height])

vehicles.sort(reverse=True) # vehicles 리스트를 큰 값부터 작은 값 순서로 정렬

img = plt.imread("18396708_frame_125.png")

plt.imshow(img) # 읽은 이미지를 화면에 표시

ax= plt.gca() # 현재 이미지가 그려진 좌표축 가져오기
#vehicles[0] 0번 인덱스가 가장큰거
size,x,y,width,height = vehicles[0]
box = patches.Rectangle(
    (x,y),
    width,
    height,
    fill=False,
    edgecolor='red',
    linewidth=2
)
ax.add_patch(box)
#[2] 세번째 크기
size,x,y,width,height = vehicles[2]
box = patches.Rectangle(
    (x,y),
    width,
    height,
    fill=False,
    edgecolor='yellow',
    linewidth=2
)
ax.add_patch(box)
plt.show()