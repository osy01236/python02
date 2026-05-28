import cv2
import numpy as np

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

#차량 주행중 ㅂ빨간 신호등 발견되면 멈추라고 경고 하기
#영상에서 특정 색상을 구별하기

cap = cv2.VideoCapture("yolo/videos/traffic_red.mp4")

fr_ct = 0

while True : 
    ret , fr = cap.read()
    if not ret : break

    fr_ct += 1

    fr= cv2.resize(fr , (480, 640))

    results = model(fr , classes = [ 9 ] , conf = 0.2)

    boxs = results[0].boxes

    red_light = False

    for box in boxs :
        x1, y1, x2, y2 = map(int , box.xyxy[0])

        if y1 > 300:
            continue

        roi = fr[y1:y2 , x1:x2] #프레임에서 신호등 영역만 가져오기

        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        lower_red1 = np.array([0, 120, 70])
        upper_red1 = np.array([10, 255, 255])

        lower_red2 = np.array([170, 120, 70])
        upper_red2 = np.array([180, 255, 255])

        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

        red_mask = mask1 + mask2
        red_pixel = cv2.countNonZero(red_mask)
        
        if red_pixel > 50 :
            red_light = True
            cv2.rectangle(fr , (x1,y1) , (x2,y2) , (0,0,255) , 3)

    if red_light :
        blink_on = (fr_ct // 5) % 2 == 0

        if blink_on :
            red_overlay = np.zeros_like(fr)
            red_overlay[:] = (0, 0, 255)

            fr = cv2.addWeighted(fr, 0.65, red_overlay, 0.35, 0)
        cv2.putText(fr, "STOP!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 8)
    

    cv2.imshow("yolo" , fr)

    if cv2.waitKey(30) == 27 :
        break

cap.release()
cv2.destroyAllWindows()