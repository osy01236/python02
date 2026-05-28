import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("yolo/videos/cup.mp4")

_, target_frame = cap.read()
res = model(target_frame)
boxs = res[0].boxes

dec_name = []
for box in boxs:
    cid = int(box.cls[0])
    dec_name.append(f"{cid}. {model.names[cid]}")

for name in dec_name:
    print(name)

sel_object = list(
    map(
        int,
        input("탐지 객체번호 입력 : ").split()
    )
)

cap = cv2.VideoCapture("yolo/videos/cup.mp4")
while True:
    r, fr = cap.read()
    if not r: break
    fr = cv2.resize(fr, (480,640))

    results = model.predict( 
        fr, classes=sel_object
    )
    res = results[0].plot()
    cv2.imshow("yolo", res)
    if cv2.waitKey(30) ==27:break

cap.release()
cv2.destroyAllWindows()



#==============================================================================
# names = model.names

# results = model("yolo/images/img1.jpg")

# results[0].show()

# print(results[0].boxes)



#==============================================================================
# names = model.names

# find_object = []
# find = input("탐지 객체명 입력 : ")

# for k, v in names.items():
#     if v in find:
#         find_object.append(k)

# results = model("yolo/images/handbag.jpg" , classes=find_object , conf=0.6)

# results[0].show()

#=============================================================================

