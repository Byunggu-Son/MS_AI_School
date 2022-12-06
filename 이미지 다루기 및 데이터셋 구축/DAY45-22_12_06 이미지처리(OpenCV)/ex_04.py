# 흑백 이미지 대비 높이기
import cv2
import matplotlib.pyplot as plt

image_path = './cat.jpg'

# # 이미지 대비 높이기
# image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# image_enhanced = cv2.equalizeHist(image_gray)

# # plot
# fig, ax = plt.subplots(1,2, figsize=(10,5))

# ax[0].imshow(image_gray, cmap='gray')
# ax[0].set_title('Original Image')
# ax[1].imshow(image_enhanced, cmap='gray')
# ax[1].set_title('Enhanced Image')
# plt.show()
# # 히스토그램 평활화는 잘 안쓴다고 한다.


### 컬러 이미지 대비 높이기
# 방법 : BGR -> YUV 컬러 포맷으로 변환 -> equalizeHist() -> RGB
# matplotlib에서는 BGR로 값을 받기 때문에 이렇게 한 듯.
# RGB거치지 않고 BGR -> YUV로 바로 전환해도 결과값에 대한 차이는 없었다.

image_bgr = cv2.imread(image_path)

# RGB
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# YUV
image_yuv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YUV)

# 히스토그램 평활화 적용
image_yuv[:, :, 0] = cv2.equalizeHist(image_yuv[:, :, 0])

# RGB 변경
image_rgb_temp = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2RGB)

# plot
fig, ax = plt.subplots(1,2, figsize=(10,5))
ax[0].imshow(image_rgb)
ax[0].set_title('Original Image')
ax[1].imshow(image_rgb_temp)
ax[1].set_title('Enhanced Image')
plt.show()




