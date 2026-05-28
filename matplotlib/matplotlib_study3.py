
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import json


# img = Image.open("18396603_frame_20.png")

#json 파일 읽어서 사람 위치 찾기
with open('18396603_frame_20.json','r',encoding='utf-8') as f:
    data = json.load(f)

annotations = data['frames']['annotations']

pos = None

for ann in annotations:
    code = ann['category']['code']
    if 'person' != code:
        continue
    label = ann['label']
    pos = (
        label['x'],
        label['y'],
        label['width'],
        label['height']
    )

img = plt.imread('18396603_frame_20.png')

plt.imshow(img) # 이미지 출력

# plt.axis("off")
# 이미지 좌표 가져오기
ax= plt.gca()

#박스 좌표 설정
# x = 400
# y = 400
# width = 200
# height = 400
x,y,width,height = pos


#사각형 박스 만들기
box = patches.Rectangle(
    (x,y), #시작 좌표
    width,  #너비
    height, #높이
    fill=False, #박스 내부 색 채우기 여부
    edgecolor='red', #박스 테두리 색
    linewidth=2 #테두리 선 굵기
)
ax.add_patch(box)
plt.show()