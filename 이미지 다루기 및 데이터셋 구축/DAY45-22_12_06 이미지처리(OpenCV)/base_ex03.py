# 이미지 선명하게 보기
import cv2
import numpy as np
from utils import image_show

image = cv2.imread('./car.jpg')

# Creating out sharpening filter
filter = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])

sharpen_img = cv2.filter2D(image, -1, filter)
# 얼마나 선명해졌는지 원본과 비교
cv2.imshow('origin image', image)
cv2.waitKey(0)
image_show(sharpen_img)