# 가우시안 필터 적용
import cv2
import numpy as np
from utils import image_show

img = cv2.imread('./car.jpg', 0)
print(img.shape)
img_rsize = cv2.resize(img, (320, 240))

# 가우시안 블러는 홀수값만 받는다.
# 그냥 블러와의 차이는 가우시안이 조금 더 선명하다.
# 수학적 공식에 의해서 짝수는 안 받는 것 같다.

Gaussian_blurred_1 = np.hstack([
    cv2.GaussianBlur(img_rsize, (3,3), 0),
    cv2.GaussianBlur(img_rsize, (5,5), 0),
    cv2.GaussianBlur(img_rsize, (9,9), 0)])

image_show(Gaussian_blurred_1)
cv2.imwrite("gaussian_blur.png", Gaussian_blurred_1)