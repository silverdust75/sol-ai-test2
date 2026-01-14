import cv2
import matplotlib.pyplot as plt

# 1. 이미지 로드
img = cv2.imread("v05_data_aug/inputjpg.jpg")

# 2. 이미지 전처리
# 2-1. 이미지 전처리 (수평 반전)
img_flipped = cv2.flip(img, 1)
#1 = 수평, 0= 수직, -1= 수평+수직

# 2-2. 이미지 전처리
img_0flip = cv2.flip(img, 0)
# 2-3. 이미지 전처리
img_11flip = cv2.flip(img, -1)

# 3. 이미지 시각화
fig, ax = plt.subplots(2,2, figsize=(10,5)) 
# subplots(2,2...= 0.0 0.1 1.0 1.1 4칸만 존재함
#subplots(2,2의 칸수에 주의 할것.

# 3-1. 원본 이미지
ax[0,0].imshow(cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
ax[0,0].axis('off')
ax[0,0].set_title("Original")

ax[0,1].imshow(cv2.cvtColor(img_flipped, cv2.COLOR_RGB2BGR))
ax[0,1].axis('off')
ax[0,1].set_title("filp")

ax[1,0].imshow(cv2.cvtColor(img_0flip, cv2.COLOR_RGB2BGR))
ax[1,0].axis('off')
ax[1,0].set_title("0filp")

ax[1,1].imshow(cv2.cvtColor(img_11flip, cv2.COLOR_RGB2BGR))
ax[1,1].axis('off')
ax[1,1].set_title("11filp")

plt.show()

# 4. 이미지 저장
cv2.imwrite("./img_flipped.jpg", img_flipped)
cv2.imwrite("./img_0flip.jpg", img_0flip)
cv2.imwrite("./img_11flip.jpg", img_11flip)
print("이미지 저장 완료")