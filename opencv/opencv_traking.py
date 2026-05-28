
'''
BOOSTING: 오래된 방식, 느리고 정확도 낮음
MIL: 비교적 기본적인 추적기
KCF: 빠르고 많이 쓰임
CSRT: 정확도 좋지만 조금 느림
MOSSE: 매우 빠름, 정확도는 낮을 수 있음
'''
import cv2
import math
# import numpy as np



#객체 추적  - 움직이는 객체를 추적하기

cap = cv2.VideoCapture("opencv/videos/video3.mp4")

bgdl = cv2.createBackgroundSubtractorMOG2( #배경 제거용
    history=300, #배경을 학습할 프레임 수
    varThreshold=35, #얼마나 달라져야 움직임으로 판단하는지?
    detectShadows=True #그림자 처리 여부
)

#객체 추적용
next_id = 1
objects = {} # id = (x,y)
max_dist =150
max_miss = 180


while True:
    ret , frame = cap.read()
    if not ret : break

    frame = cv2.resize( frame, (480,640))

    fgmask = bgdl.apply(frame) #배경 제거

    _, thresh = cv2.threshold( 
        fgmask, 200 ,255 ,cv2.THRESH_BINARY )

    #모폴로지 작업
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

    fmask = cv2.morphologyEx( #노이즈 제거 (작은점 제거)
        thresh, cv2.MORPH_OPEN, kernel , iterations=1
    ) 
    
    #모폴리지 연결
    mask = cv2.morphologyEx( #끊어진 움직임 영역 연결
        fmask, cv2.MORPH_CLOSE, kernel, iterations=2)
    
    contours , _ =  cv2.findContours(
        mask, cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_SIMPLE
    )

    copy= frame.copy()
    detections = []


    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area <30 : continue

        x,y,w,h = cv2.boundingRect(cnt)

        if h > w*2 :
            continue

        #움직이느 객체의 중심점 찾기
        cx = x + w //2
        cy = y + h //2

        detections.append({
            "x": x,
            "y": y,
            "w": w,
            "h": h,
            "cx": cx,
            "cy": cy
        })

    for obj_id in objects :
        objects[obj_id]["miss"] +=1

    used_ids = set()

    for det in detections:
        cx = det["cx"]
        cy = det["cy"]

        match_id = None
        min_dist = 10000

        for obj_id, obj in objects.items():
            if obj_id in used_ids:
                continue
            old_cx = obj["cx"]
            old_cy = obj["cy"]

            dist = math.hypot(cx - old_cx , cy - old_cy)

            if dist < min_dist and dist < max_dist:
                min_dist = dist
                match_id = obj_id
       
        if match_id is None :
            match_id = next_id
            next_id +=1

        objects[match_id] = {
            "cx":cx,
            "cy":cy,
            "miss":0,
            "x":det["x"],
            "y":det["y"],
            "w":det["w"],
            "h":det["h"]
        }
        used_ids.add(match_id)
    
    delete_ids = []
   
    for obj_id, obj in objects.items():
        if obj["miss"] >max_miss:
            delete_ids.append(obj_id)
    
    for obj_id in delete_ids:
        del objects[obj_id]

    for obj_id, obj in objects.items():
        if obj["miss"] > 0:
            cv2.circle(copy, (obj["cx"], obj["cy"]), 5, (80,80,255),-1)
            cv2.putText( copy, f"ID{obj_id}", (obj["cx"], obj["cy"] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,200),1    )

            continue

        x=obj["x"]
        y=obj["y"]
        w=obj["w"]
        h=obj["h"]

        cv2.rectangle( copy, (x,y), (x+w, y+h), (0,0,255), 2)
        cv2.circle(copy, (obj["cx"], obj["cy"]), 4, (0,0,255),-1)
        cv2.putText( copy, f"ID{obj_id}", (x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,200),2)

    cv2.imshow("frame", frame)
    cv2.imshow("thresh", thresh)
    cv2.imshow("bbox", copy)




    if cv2.waitKey(int (1000/60)) ==27:
        break

cap.release()
cv2.destroyAllWindows()