# 같은 크기의 이미지 블렌딩 실험
import cv2
import matplotlib.pyplot as plt
import numpy as np

large_img = cv2.imread('./ex_image.png')
watermakr = cv2.imread('./ex_image_logo.png')

# 이미지 사이즈 확인 -> 크기가 다르므로 resize해준다.
print('large_image size >>', large_img.shape) # 높이, 넓이, 채널값 확인
print('watermakr image size >>', watermakr.shape)

# cv2.imshow("image large", large_img)
# cv2.imshow("watermakr", watermakr)
# cv2.waitKey(0)

########### 이미지 크기 수정 #############
img1 = cv2.resize(large_img,(800,600))
img2 = cv2.resize(watermakr,(800,600))

print('large_image resize >>', img1.shape)
print('watermakr image resize >>', img2.shape)

# cv2.imshow("image large", img1)
# cv2.imshow("watermakr", img2)
# cv2.waitKey(0)

########## 이미지 혼합 진행 #################
# alpha와 beta 사용 (덜 투명하게 할건지에 대해 정함.)

# # 베이스 5:5
blended = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imshow("image show", blended)
cv2.waitKey(0)

# # 베이스 9:1
blended = cv2.addWeighted(img1, 9, img2, 1, 0)
# cv2.imshow("image show", blended)
# cv2.waitKey(0)

# # 1로 설정
blended = cv2.addWeighted(img1, 1, img2, 1, 0)
# cv2.imshow("image show", blended)
# cv2.waitKey(0)
