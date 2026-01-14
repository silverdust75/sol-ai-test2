from PIL import Image, ImageEnhance, ImageOps
import matplotlib.pyplot as plt

# 1. 이미지 로드
img = Image.open("captired_images/result_20260113_152623.jpg")

# 2. 이미지 전처리
img_rotated = img.rotate(90)

# 2-1. 이미지 밝기
enhancer = ImageEnhance.Brightness(img)
# 밝기의 경우 위와 같이 먼저 이미지를 밝기를 올리겠다고 불어와야함.

img_Enhance = enhancer.enhance(1.5)


# 2.2. 이미지 좌우 반전
img_Ops = ImageOps.mirror(img)

# 3. 결과 시각화
fig, ax = plt.subplots(2, 3, figsize=(20, 10))

# 원본 이미지
ax[0,0].imshow(img)
ax[0,0].axis('off')
ax[0,0].set_title("Original")

# 회전 이미지
ax[0,1].imshow(img_rotated)
ax[0,1].axis('off')
ax[0,1].set_title("Rorared 90도")
# 밝기 이미지
ax[0,2].imshow(img_Enhance)
ax[0,2].axis('off')
ax[0,2].set_title("Brightness 10")
# 좌우 반전 이미지
ax[1,0].imshow(img_Ops)
ax[1,0].axis('off')
ax[1,0].set_title("Ops.mirror")

plt.show()

img_rotated.save("./img_rotated.jpg")
# 이미지 밝기 저장
img_Enhance.save("./img_Enhance.jpg")
# 이미지 좌우 반전
img_Ops.save("./img_ops.jpg")
print("이미지 저장이 잘 됐습니다.")