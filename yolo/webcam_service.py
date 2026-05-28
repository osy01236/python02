import cv2
import os
from datetime import datetime

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

streaming = True


def stop_record():
    global streaming
    streaming = False


def record_frames():
    global streaming
    streaming = True

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return

    # 영상 저장은 cv2.VideoWriter 함수 사용
    # 영상 저장하려면 저장파일 이름, 확장자, fps, 영상크기 필요
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # YOLO 분석 때문에 실제 저장되는 프레임 수가 낮아서 FPS를 낮게 고정
    fps = 5
    
    # fps = int(cap.get(cv2.CAP_PROP_FPS))

    # if fps == 0:
    #     fps = 30

    os.makedirs("videos", exist_ok=True)

    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    video_path = os.path.join("videos", f"cam_{now}.mp4")
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    writer = cv2.VideoWriter(
        video_path,
        fourcc,
        fps,
        (width, height)
    )

    if not writer.isOpened():
        print("VideoWriter를 열 수 없습니다.")
        cap.release()
        return

    while streaming:
        ret, frame = cap.read()

        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        results = model(frame, verbose=False)
        res = results[0].plot()    
        writer.write(res)

        success, buffer = cv2.imencode(
            ".jpg",
            res ,
            [cv2.IMWRITE_JPEG_QUALITY, 80],
        )

        if not success:
            continue

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + buffer.tobytes()
            + b"\r\n"
        )

    writer.release()
    cap.release()