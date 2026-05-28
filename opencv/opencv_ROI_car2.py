import cv2
import numpy as np

cap = cv2.VideoCapture("opencv/videos/motion_car.mp4")

paused = False #영상 일시 정지용
roi_point = [] # 좌표 저장용
current_frame = None  
display = None

mask_enabled = False 

def mouse_pos(event, x , y , flag , param):
    global roi_point , display, mask_enabled
    if event == cv2.EVENT_LBUTTONDOWN:  
        
        roi_point.append((x,y)) #마우스 클릭 좌표 저장
        cv2.circle(display , (x,y), 5, (0,255,150),-1)

        if len(roi_point) >= 2: #좌표 두번 이상클릭했다면
            cv2.line(
                display,
                roi_point[-2],
                roi_point[-1],
                (255,0,0),2
            )
    elif event == cv2.EVENT_RBUTTONDOWN:
        if len(roi_point ) >= 3:
            mask_enabled= True
            cv2.line(display, roi_point[-1], roi_point[0],
                     (255,0,0),2)


cv2.namedWindow("car")
cv2.setMouseCallback("car", mouse_pos)
bgdelete = cv2.createBackgroundSubtractorMOG2(
    history=300,        #  배경을 학습할 프레임 수
    varThreshold=40,    #  얼마나 달라져야 움직임으로 판단하는지?
    detectShadows=False #그림자 처리 여부

)


while True:
    if not paused: # 일시 정지가 아니면 다음 프레임 읽기
        ret, frame = cap.read()
        if not ret :break
        frame = cv2.resize( frame , None , fx=0.5 , fy= 0.5)
        
        current_frame = frame.copy()
        display = frame.copy()
        if mask_enabled :
            pts = np.array(roi_point, np.int32)
            
            mask =np.zeros(frame.shape[:2], dtype=np.uint8)
            cv2.fillPoly(mask, [pts], 255)

            roi = cv2.bitwise_and(frame, frame, mask=mask)
            cv2.polylines(display, [pts], isClosed=True, color=(0,255,0), thickness=2)
            
            roi_gray = bgdelete.apply(roi)
            
            _,thresh = cv2.threshold(
                roi_gray, 120, 255 , cv2.THRESH_BINARY
            )
            kernel = np.ones((5,5), np.uint8)
            thresh = cv2.morphologyEx( thresh , cv2.MORPH_OPEN,
                                      kernel, iterations=1)
            thresh = cv2.morphologyEx(thresh , cv2.MORPH_CLOSE,
                                      kernel, iterations=2)
            


            contours , _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )
            for cnt in contours:
                x,y,w,h = cv2.boundingRect(cnt)
                cv2.rectangle(display, (x,y),
                              (x+w, y+h), (0,0,255),2)
            # cv2.imshow("ROI", roi)
    
    
    
    cv2.imshow("car", display)
    k = cv2.waitKey(30)
    if k == 27: break
    elif k ==32 : # 스페이스바 키 값은 32 - 일시정지용으로 사용
        paused = not paused
    elif k == ord("r"):
        roi_point = []
        if current_frame is not  None :
            display = current_frame.copy()
cap.release()
cv2.destroyAllWindows()