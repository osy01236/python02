import cv2

cap = cv2.VideoCapture("opencv/videos/video2.mp4")

while True :
    ret, frame = cap.read()
    if not ret :
        break

    frame = cv2.resize(frame, (640,480))

    blur = cv2.GaussianBlur(frame, (5,5), 0)

    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    edge = cv2.Canny(gray, 50, 150)

    cv2.imshow("original", frame)
    cv2.imshow("video", edge)
    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()