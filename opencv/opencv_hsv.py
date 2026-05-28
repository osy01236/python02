# H - Hue (색상)
# S - Saturation(채도)
# V - Value(밝기)
#빨강 - 0 , 노랑 35 , 초록 80, 파랑  130

import cv2
import numpy as np

img = cv2.imread("opencv/images/door.png")

hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0,100,100])
upper_red1 = np.array([10,255,255])


lower_red2 = np.array([170,100,100])
upper_red2 = np.array([179,255,255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1 )
mask2 = cv2.inRange(hsv, lower_red2, upper_red2 )

mask = cv2.bitwise_or(mask1, mask2)

result = cv2.bitwise_and(img, img, mask=mask)

contours , _ = cv2.findContours(
    mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)


box = img.copy()
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 10000: continue
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(box, (x,y), (x+w, y+h), (0,255,0), 3)
    

# re_mask = cv2.bitwise_not(mask)

cv2.imshow("box", box)
cv2.imshow("result", result)
# cv2.imshow("mask", mask)
# cv2.imshow("mask2", mask2)
# cv2.imshow("re_mask", re_mask)
cv2.imshow("original", img)
cv2.imshow("hsv", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()