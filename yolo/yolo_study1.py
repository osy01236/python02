from ultralytics import YOLO

#ultralytics yolo 모델 크기
#n : 가장 가벼움 
#s : n보다 조금더
#m : 중간 크기 pc성능 좋아야함
#l : 많은 학습이 되어있음
#x : 최상위 모델, AI 전용 서버에서 운영 가능


import cv2
#================================================ 이미지 파일로 다룬것 ================================================
# model = YOLO("yolov8n.pt")
# results = model("yolo/images/dog.png" )
# img = results[0].plot()

# print(model.names)

# small = cv2.resize(img, None , fx=0.5 , fy=0.5)

# cv2.imshow("dodododododog", small)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#================================================


model = YOLO("yolov8n.pt")

# results = model("yolo/videos/bird.mp4" ,stream=True)

cap = cv2.VideoCapture("yolo/videos/bird.mp4")

while True:
    ret, frame = cap.read()
    if not ret :
        break

    frame = cv2.resize(frame, (480,640))
    
    result = model(frame)
    
    anno = result[0].plot()

    cv2.imshow("bird", anno)
    
    key=cv2.waitKey(30)
    
    if key == 27:
        break
cap.release()




cv2.destroyAllWindows()