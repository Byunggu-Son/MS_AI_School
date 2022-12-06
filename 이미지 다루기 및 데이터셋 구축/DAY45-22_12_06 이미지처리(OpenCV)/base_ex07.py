# 엠보싱 필터
import cv2
import numpy as np
from utils import image_show

img_path = './car.jpg'
img = cv2.imread('./car.jpg')


# 엠보싱 효과
filter1 = np.array([[0,1,0],[0,0,0],[0,-1,0]])
filter2 = np.array([[-1,-1,0],[-1,0,1],[0,1,1]]) # 엠보싱 필터로는 이 두개를 제일 많이 쓴다고 한다.
emboss_img = cv2.filter2D(img, -1, filter1)
emboss_img = emboss_img + 128 # fiilter1쓸 경우에만 켜기.
image_show(emboss_img) # filter1에서 그냥 엠보싱만 하면 엠보싱이 잘 안보여서 +128해서 회색조 만들어 준다.
