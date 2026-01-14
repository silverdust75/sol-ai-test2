from ultralytics import YOLO

#모델
model = YOLO("yolo11n-cls.pt")

#학습
model.train(
    data="testdataset",
    epochs=20,
    batch=10,
    imgsz=256,
)
