import cv2
# 문제 1: 영상 3초 지점 캡처하기

#bird.mp4에서 3초 지점의 프레임을 이미지로 저장하세요.

#조건: target_sec = 3

# 영상 파일 열기
cap = cv2.VideoCapture("opencv/videos/bird.mp4")

# 영상의 FPS 가져오기
# FPS는 1초에 몇 프레임인지 의미함
fps = cap.get(cv2.CAP_PROP_FPS)

# 캡처하고 싶은 시간, 여기서는 3초
target_sec = 3

# 3초 지점의 프레임 번호 계산
# 예: fps가 30이면 3초는 90번째 프레임
target_frame_num = int(fps * target_sec)

# 영상의 현재 위치를 target_frame_num 프레임으로 이동
cap.set(cv2.CAP_PROP_POS_FRAMES, target_frame_num)

# 이동한 위치에서 프레임 한 장 읽기
ret, frame = cap.read()

# ret이 True면 프레임을 정상적으로 읽었다는 뜻
if ret:
    # 읽은 프레임을 이미지 파일로 저장
    cv2.imwrite("opencv/images/bird_3sec.jpg", frame)
    print("3초 지점 캡처 완료")
else:
    print("프레임을 읽지 못했습니다.")

# 영상 파일 닫기
cap.release()

# 열린 OpenCV 창이 있다면 모두 닫기
cv2.destroyAllWindows()

#문제 2: lane 이미지에서 Canny 값 바꿔보기

#opencv_study3.py를 참고해서 lane.png 이미지에서 edge를 찾으세요.

#조건:이미지를 읽는다.
#     흑백으로 바꾼다.
#     블러 처리한다.
#     Canny를 2개 만든다.


# 이미지 읽기
img = cv2.imread("opencv/images/lane.png")

# 이미지를 흑백으로 변환
# Canny는 보통 흑백 이미지에서 사용함
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 이미지에 블러 처리
# 노이즈를 줄여서 edge가 너무 지저분하게 나오지 않게 함
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Canny edge 검출 1
# 숫자가 낮으면 약한 경계선도 많이 잡힘
edge1 = cv2.Canny(blur, 30, 100)

# Canny edge 검출 2
# 숫자가 높으면 강한 경계선 위주로 잡힘
edge2 = cv2.Canny(blur, 100, 250)

# 원본 흑백 이미지 출력
cv2.imshow("gray", gray)

# 낮은 기준값으로 edge 검출한 결과
cv2.imshow("edge1", edge1)

# 높은 기준값으로 edge 검출한 결과
cv2.imshow("edge2", edge2)

# 키 입력이 있을 때까지 창 유지
cv2.waitKey(0)

# 모든 창 닫기
cv2.destroyAllWindows()