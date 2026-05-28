import numpy as np
import matplotlib.pyplot as plt
from fontTools.merge import cmap
#
# img= np.array([
#     [0,50,10],
#     [150,200,255]
# ])
img = np.random.randint(0, 256, (100, 100))

# bright = np.clip(img-100,0,255)#clip  범위 지정하고 그범위를 넘지않게하는 함수
# bright = 255 - img #반전 효과
#128이상은 255변경, 128미만은 0변경
copy_img = img.copy() #원본복사
copy_img[copy_img >= 128] =255
copy_img[copy_img < 128] = 0

plt.figure(figsize=(8,4))

plt.subplot(1,2,1) #1행 2열 에서 1열 에 배치
plt.imshow(copy_img ,cmap='gray')
plt.title("copy")
plt.axis('off')

plt.subplot(1,2,2) #1행 2열 에서 2열 에 배치
plt.imshow(img ,cmap='gray')
plt.title("original")
plt.axis('off')

plt.show()