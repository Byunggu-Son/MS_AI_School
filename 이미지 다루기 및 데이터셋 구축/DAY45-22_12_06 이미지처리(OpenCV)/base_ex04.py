# 이미지 선명하게 보기 - 샤프닝 필터 버전 – 멕시칸 햇 또는 라플라시안 필터
import cv2
import numpy as np
from utils import image_show

image = cv2.imread('./car.jpg')

# Creating maxican hat filter for
# 5X5
filter = np.array([[0,0,-1,0,0],[0,-1,-2,-1,0],[-1,-2,16,-2,-1],[0,-1,-2,-1,0],[0,0,-1,0,0]])

# 3x3
# filter = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

mexican_hat_image = cv2.filter2D(image, -1, filter)
image_show(mexican_hat_image)
cv2.imwrite('./mexican_hat_5X5.png', mexican_hat_image)
# cv2.imwrite('./mexican_hat_3X3.png', mexican_hat_image)
# 라플라시안 마스크는 참고자료를 보고 이해하자!(3X3, 5X5에 대한 값)
# 5X5와 3X3 선명도 비교