import cv2
import time

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("yolo/videos/pedestrian1.mp4")

person_hg = 1.72 #사람의 키
focal = 400 #카메라 초첮

while True:
    ret, fr = cap.read()
    if not ret: break

    fr = cv2.resize(fr, (640, 480))

    result = model(fr , classes=[0,2])

    boxs = result[0].boxes

    for box in boxs:
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        dist = (person_hg * focal) / (y2 - y1)

        cv2.putText(fr, f"{dist:.2f}m", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        cv2.rectangle(fr, (x1, y1), (x2, y2), (0, 0, 255), 2)

        if dist <= 10:
            blink = int(time.time() * 4 )%2
            if blink == 0:
                red_overlay = fr.copy()
                red_overlay[:,:] = (0,0,255)

                fr = cv2.addWeighted(fr, 0.65, red_overlay, 0.35, 0)


    cv2.imshow("frame", fr)

    k = cv2.waitKey(30)
    if k == 27: break

cap.release()
cv2.destroyAllWindows()