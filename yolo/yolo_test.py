from ultralytics import YOLO

import cv2

model = YOLO("yolov8m.pt")

video_donut = "yolo/videos/donut.mp4"

cap = cv2.VideoCapture(video_donut)

#.1 영상 첫 프레임에서 객체 목록 찾기

# 1-1 영상에서 첫번쨰 프레임 사진 읽어서  
_, target_frame = cap.read()

# 1-2 객체 탐지를 실행
res = model(target_frame)

# 1-3 탑지된 객체 박스 정보 가져오고
boxs= res[0].boxes

# 1-4 탐지된 객체이름을 저장할 리스트 , 튜블 , 세트 (set은 중복제거함) , 딕셔너리
dec_name = {} #딕셔너리

# 1-5 탐지된 객체 하나씩 꺼내오고
for box in boxs :

    # 1-6 객체의 클래스 번호 가져오기
    #예 )0 = person,
    cid = int(box.cls[0])

    # 1-7클래스 번호 , 이름을 저장
    dec_name[cid] = model.names[cid]

#위의 첫 프레임에 탐지된 객체 목록 출력
print("=======객체 목록 ========")

for k, name in dec_name.items():
    print(k ,name)

cap.release()



# =====================================================
# 2. 사용자가 탐지할 객체 번호 입력하는 부분
# =====================================================


sel_object = list(
    map(
        int,
        input("탐지 객체번호 입력 : ").split()
    )
)

# =====================================================

cap = cv2.VideoCapture(video_donut)

while True:
    # 영상에서 프레임을 한 장씩 읽기
    r, fr = cap.read()

    # 더 이상 읽을 프레임이 없으면 반복 종료
    if not r:
        break

    # 화면 크기 조절
    fr = cv2.resize(fr, (480,640))

    # 사용자가 입력한 객체 번호만 탐지
    # classes=sel_object 이 부분이 핵심
    results = model.predict(
        fr,
        classes=sel_object,
        verbose=False
    )

    # 탐지 결과를 이미지에 그리기
    res = results[0].plot()

    # 결과 화면 출력
    cv2.imshow("yolo", res)

    # ESC 키를 누르면 종료
    if cv2.waitKey(30) == 27:
        break

# 영상 닫기
cap.release()

# 모든 OpenCV 창 닫기
cv2.destroyAllWindows()