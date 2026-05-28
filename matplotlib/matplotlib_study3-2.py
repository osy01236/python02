
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import json

from PIL.ImageOps import pad
from matplotlib import colors

# img = Image.open("18396603_frame_20.png")

#json 파일 읽어서 사람 위치 찾기
with open('18396603_frame_20.json','r',encoding='utf-8') as f:
    data = json.load(f)

annotations = data['frames']['annotations']

colors = ('red', 'green', 'blue', 'yellow','lime','magenta','cyan','purple')
pos = list()
idx=0
for ann in annotations:
    code = ann['category']['code']
    if 'vehicle' != code:
        continue

    label = ann['label']
    pos.append((
        label['x'],
        label['y'],
        label['width'],
        label['height'],
        colors[idx]))
    idx+=1
print(pos)
# x,y,width,height = pos
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
# x,y,width,height = pos
for x,y,w,h,color in pos:

#사각형 박스 만들기
    box = patches.Rectangle(
        (x,y), #시작 좌표
        w,  #너비
        h, #높이
        fill=False, #박스 내부 색 채우기 여부
        edgecolor=color, #박스 테두리 색
        linewidth=2 #테두리 선 굵기
    )
    ax.add_patch(box)
    #바운딩 박스위에 테긋트 넣기
    plt.text(x,y-10,'object',color='red',
             fontsize=10,
             bbox=dict(facecolor='white',edgecolor='red',pad=2))

plt.show()