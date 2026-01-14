from ultralytics import YOLO

# 1. 데이터셋 준비
# dataset/
#ㅣ-train
#      ㅣ-Class1(출력명 : 예)person)
#             ㅣ-Class1.jpg
#             ㅣ-Class1.jpg
#             ㅣ-Class1.jpg
#             ㅣ-Class1.jpg
#      ㅣ-Class2(dog)
#             ㅣ-Class2.jpg
#             ㅣ-Class2.jpg
# ㅣ-val/
#     #ㅣ-Class1(person)
#             ㅣ-Class1.jpg
#             ㅣ-Class1.jpg
#             ㅣ-Class1.jpg
#             ㅣ-Class1.jpg
#      ㅣ-Class2(dog)
#             ㅣ-Class2.jpg
#             ㅣ-Class2.jpg
#ㅣ-test/

model = YOLO("yolo11n-cls.pt")

# 2. 모델 학습
model.train(
    data="dataset", #데이터셋 경로
    epochs=2, #학습 획수
    batch=1, # 배치 사이즈
    imgsz=256, #이미지 크기
)

# Happy, Sad, Normal 표정 분류 모델
# 이미지 크기 : 256
# 배치 사이즈 : free
# epochs : free

