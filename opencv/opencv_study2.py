#AI가 영상 분석을 하는데 먼저 전처리 한다.
#전처리 는 크기 변경, 흑백변환, 노이즈 제거, 강조 처리 등

import cv2

# img = cv2.imread("opencv/images/surfing.png")

#변경 이후에 show
# 흑백 변환 - cv2.COLOR_BGR2GRAY
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow("surfer", gray)
# print( gray.shape)
# print( gray[100][100])
# cv2.waitKey(0)

#크기 변경하기

# small = cv2.resize(img, (400,100))
# cv2.imshow("resize", small)
# print(small.shape)
# cv2.waitKey(0)

# 이미지 뒤집기 (반전)

# flip = cv2.flip(img, 1)
# # 1 -> 좌우반전, 0 -> 상하반전 , -1  -> 상하 + 좌우반전

# # 블러 처리 - 이미지 흐리게 만드는것
# # 노이즈 감소의 목적
# blur = cv2.GaussianBlur(img, (5,5), 0)
# # (5,5) 의 값을 크게 주면 더더 흐려진다.

# cv2.imshow("bulr",blur)
# cv2.waitKey(0)

# 경계 - threshold

# gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)

# _,thresh =cv2.threshold(
#     gray, 127 , 255, cv2.THRESH_BINARY
# )
# _,thresh_rev = cv2.threshold(
#     gray, 127,255, cv2.THRESH_BINARY_INV
# )

# cv2.imshow("gray",gray)
# cv2.imshow("bin",thresh)
# cv2.imshow("inv",thresh_rev)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 사진의 크기는 가로길이 320 으로 비율 유지해서 변경하고
# 흑백 변환하고 , 멍멍이가 잘 보일수 있도록 경계설정하여
# dog_result.png로 저장하기

img = cv2.imread("opencv/images/dog.png")


h, w = img.shape[:2]

# 2016 : 1512 = 320 : x
hh = int((1512 * 320)/2016) 
ww = 320

resize_img = cv2.resize(img, (ww,hh))

gray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)

_,thresh =cv2.threshold(
     gray, 140 , 255, cv2.THRESH_BINARY
)
_,thresh_rev = cv2.threshold(
     gray, 160 , 255 , cv2.THRESH_BINARY_INV
)


cv2.imshow("dog1", resize_img)
cv2.imshow("dog2", gray)
cv2.imshow("dog3", thresh)
cv2.imshow("dog4", thresh_rev)
print( gray.shape)

cv2.waitKey(0)

cv2.destroyAllWindows()