from ultralytics import YOLO
import cv2

# 1. 모델 로드
model = YOLO("yolo11n-cls.pt")
# 2. 모델 추론
results = model("v07_1_yolo_basic\input2.jpg")
results2 = model("v07_1_yolo_basic\input3.jpg")

# 3. 결과 확인
results_image = results[0].plot()
results_image2 = results2[0].plot()

# 4. 결과 이미지 저장
output_image_path = "./result2.jpg"
output_image_path2 = "./results3.jpg"
cv2.imwrite(output_image_path, results_image)
cv2.imwrite(output_image_path2, results_image2)
print(f"예측 결과 이미지가 잘 저장 되었습니다. {output_image_path}")