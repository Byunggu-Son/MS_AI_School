import cv2
from utils import image_show

image_path = "./cat.jpg"
image_gary = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#read하면서 변경하는 방법으로(read하고 밑에서 변경할 수도 있는데 갠취.)

image_10x10 = cv2.resize(image_gary, (10, 10))
image_10x10.flatten() # 이미지 데이터를 1차원 백터로 변환.
image_show(image_10x10)
