#region of Interest - 관심영역 - 영상이나 이미지에서 특정 영역만 분석하기위함
#특정영역을 잘라내는방법은 numpy 배열 자르기 (slicing)
#특정영역 지정하는 방법 4가지
#1. 마우스 또는 손가락으로 영역 지정하기
#2. 그림판, 포토샵 , 캡처툴 사용
#3. 직접 rect 그려서 맞춰 나가기
#4. shape 기준으로 계산


import cv2

#마우스 클릭 함수


img = cv2.imread("opencv/images/door.png")


point = [] # 두 좌표 저장용
def mouse_pos(event, x , y , flag , param):
    global point
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"x: {x}, y : {y}")
        point.append({"x": x, "y": y})

        cv2.circle(
            img, (x,y,), 5 , (0,255,100), -1
        )
        #좌표 클릭을 2번 했다면
        if len(point ) == 2:
            p1 = point[0]
            p2 = point[1]
            cv2.rectangle( img , (p1["x"],p1["y"]),
                         (p2["x"],p2["y"]), (255,0,0), 2 )

            #ROI
            roi = img[
                min(p1["y"],p2["y"]) : max(p1["y"],p2["y"]),
                min(p1["x"],p2["x"]) : max(p1["x"],p2["x"])

            ]
            cv2.imshow("roi", roi)


cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_pos)

roi = img[200:645 , 164:335]



while True : 
    cv2.imshow("image", img)

    k=cv2.waitKey(1)
    if k == 27 :break    #27=> ESC
    if k == ord("r"):    # 키보드 r 누르면 초기화
        img = cv2.imread("opencv/images/door.png")
        point = []

cv2.destroyAllWindows()