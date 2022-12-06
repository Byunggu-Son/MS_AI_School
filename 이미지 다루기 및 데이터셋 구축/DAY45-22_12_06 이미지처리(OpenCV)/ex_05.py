import cv2
from utils import image_show

# 이미지 경로
image_path = './cat.jpg'

# 이미지 이진화
image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) # RGB로 받는 값 필요없어서 기존과 달리 바로 이진화에서 받아버린다.
max_output_value = 255
neighborhood_size = 99
subtract_from_mean = 10 # 5 
# 위의 세팅값이 보통 많이 하는 값

image_binary = cv2.adaptiveThreshold(image_gray, max_output_value,
                                     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, neighborhood_size, #cv2.THRESH_BINARY_INV 반전 효과
                                     subtract_from_mean) # adaptiveThreshold이진화 할 때 많이 사용
image_show(image_binary)