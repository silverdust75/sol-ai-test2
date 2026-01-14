from ultralytics import YOLO
import cv2

# 1.모델 로드
model = YOLO("yolo11n-seg.pt")

# 2. 모델 추론
model("v07_1_yolo_basic/city.mp4", save=True)