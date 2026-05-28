import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("yolo/videos/walk.mp4")


while True :
    ret , fr = cap.read()
    if not ret: break

    fr = cv2.resize(fr , (640,480))

    results = model(fr , classes=[0] , conf=0.5)

    boxs = results[0].boxes

    danger_rect = (0 , 240 , 100 , 400)
    cv2.rectangle(fr , (danger_rect[0] ,danger_rect[1]),
                  (danger_rect[2] ,danger_rect[3]) , (0,228,255) , 2)

    person_count = 0 

    for box in boxs :
        x1,y1,x2,y2 = map(int , box.xyxy[0])

        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2

        # if cx> danger_rect[0] and cy < danger_rect[2]:
        #     if cy >danger_rect[1] and cy < danger_rect[3]:
        if danger_rect[0] <= cx <= danger_rect[2] and danger_rect[1] <= cy <= danger_rect[3]:
                person_count+=1

        
                cv2.rectangle(fr , (x1,y1) , (x2,y2) , (0,0,255) , 2)

                cv2.putText(fr , f"ps {person_count}" , (x1,y1-10) , 
                            cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (0,255,0) , 2)
       
    

    
    cv2.putText(fr , f"total_person : {person_count}" , (20,40) ,cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0,0,255) , 2)
    cv2.imshow("frame" , fr)

    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()