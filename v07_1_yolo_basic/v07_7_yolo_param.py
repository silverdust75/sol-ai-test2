from ultralytics import YOLO
import cv2

# 1. 모델 로드
model = YOLO("yolo11n.pt")

# 모델 클래스 확인
#print(f"모델 클래스 목록 : {model.names}")

model(
    "v07_1_yolo_basic\class.jpg",
    save=True,
    classes=[67,73],
    #max_det=1
    #save_crop=True,
    #save_txt=True,
    #save_conf=True
)
# 결과 이미지를 cell phone, book만 탐지되도록