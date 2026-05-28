import cv2
import os
from datetime import datetime

from ultralytics import YOLO
from save_json import save_frame_json, flush_json


model = YOLO("yolov8n.pt")
streaming = True


def make_json(res):
    result = res[0]
    detections = []

    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cid = int(box.cls[0])
        cname = result.names[cid]
        conf = float(box.conf[0])

        detections.append({
            "class_id": cid,
            "class_name": cname,
            "confidence": round(conf, 3),
            "box": {
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2,
            },
        })

    return {
        "count": len(detections),
        "detections": detections,
    }


async def test_cam(request):
    global streaming
    streaming = True

    # 1번 카메라, 2번 카메라 열기
    # 보통 기본 카메라는 0, 추가 USB 카메라는 1입니다.
    cap1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap2 = cv2.VideoCapture(1, cv2.CAP_DSHOW)

    # JSON에 저장할 기본 정보
    save_data = {
        "info": {
            "cam1": {
                "width": int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH)),
                "height": int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                "fps": int(cap1.get(cv2.CAP_PROP_FPS)),
            },
            "cam2": {
                "width": int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH)),
                "height": int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                "fps": int(cap2.get(cv2.CAP_PROP_FPS)),
            },
        },
        "frames": [],
    }

    frame_no = 0

    # 현재 분 단위로 JSONL 파일 생성
    current_minute = datetime.now().strftime("%Y%m%d_%H%M")
    json_path = os.path.join("records", f"cam_{current_minute}.jsonl")

    while streaming:
        # 브라우저 연결이 끊기면 반복 종료
        if await request.is_disconnected():
            break

        # 두 카메라에서 프레임 읽기
        ret1, fr1 = cap1.read()
        ret2, fr2 = cap2.read()

        # 둘 중 하나라도 못 읽으면 종료
        if not ret1 or not ret2:
            break

        # 각 카메라 프레임을 YOLO로 분석
        results1 = model(fr1, verbose=False)
        results2 = model(fr2, verbose=False)

        frame_no += 1

        # 분이 바뀌면 기존 JSON 저장 마무리 후 새 파일로 변경
        now_minute = datetime.now().strftime("%Y%m%d_%H%M")
        if now_minute != current_minute:
            flush_json(json_path)

            current_minute = now_minute
            json_path = os.path.join("records", f"cam_{now_minute}.jsonl")

        # 두 카메라의 탐지 결과를 JSON 데이터에 저장
        save_data["frames"] = {
            "frame_no": frame_no,
            "time": datetime.now().isoformat(),
            "camera_1": make_json(results1),
            "camera_2": make_json(results2),
        }

        save_frame_json(json_path, save_data)

        # YOLO 탐지 박스가 그려진 화면 생성
        out1 = results1[0].plot()
        out2 = results2[0].plot()

        # 두 카메라 화면 크기를 맞춤
        out2 = cv2.resize(out2, (out1.shape[1], out1.shape[0]))

        # 두 화면을 좌우로 붙임
        combined = cv2.hconcat([out1, out2])

        # 브라우저 스트리밍을 위해 JPEG로 변환
        success, buffer = cv2.imencode(
            ".jpg",
            combined,
            [cv2.IMWRITE_JPEG_QUALITY, 80],
        )

        if not success:
            continue

        # FastAPI StreamingResponse로 보낼 프레임 데이터
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + buffer.tobytes()
            + b"\r\n"
        )

    # 스트리밍 종료 시 카메라 자원 해제
    cap1.release()
    cap2.release()