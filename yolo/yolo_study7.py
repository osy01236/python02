import cv2
import numpy as np

from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")

# results = model("yolo/images/dog.png")

cap = cv2.VideoCapture("yolo/videos/pedestrian2.mp4")

obj_color = {
    "person": (0, 228, 255),
    "car": (0, 0, 255)
}


while True:
    ret, fr = cap.read()
    if not ret:
        break

    fr = cv2.resize(fr, (640, 480))

    results = model(fr, classes=[0, 2], conf=0.4)

    overlay = fr.copy()

    
    if results[0].masks is not None:
        masks = results[0].masks.data
        boxs = results[0].boxes

        for mask, box in zip(masks, boxs):
            cid = int(box.cls[0])
            cname = model.names[cid]
            color = obj_color[cname]

            mask = mask.cpu().numpy()

            mask = cv2.resize(mask, (fr.shape[1], fr.shape[0]))

            mask = mask > 0.5

            overlay[mask] = color

    fr = cv2.addWeighted(fr, 0.6, overlay, 0.4, 0)

    cv2.imshow("yolo", fr)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()