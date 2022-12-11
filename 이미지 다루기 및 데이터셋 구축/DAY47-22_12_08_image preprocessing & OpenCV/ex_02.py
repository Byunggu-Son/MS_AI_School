import cv2
import numpy as np

######### ex-01 ############
# 검은색 사각형 안에 흰색 사각형
# image_rectangle = np.ones((400,400), dtype='uint8') # 검은색 정사각형 생성
# cv2.rectangle(image_rectangle, (50,50),(300,300),(255,255,255), -1) # 안에 들어갈 흰색 사각형
# cv2.imshow("image show", image_rectangle)
# cv2.waitKey(0)


######### ex-02 ############
# 검은색 사각형 안에 흰색 원
# img_circle = np.ones((400,400), dtype='uint8')
# cv2.circle(img_circle, (300,300), 70, (255,255,255), -1)
# cv2.imshow("image show", img_circle)
# cv2.waitKey(0)

######### ex-03 ############
#### 비트 연산에 대해 알아보자.(합,교집합으로 쉽게 이해)
# 위에 2줄씩 가져옴.
img_rectangle = np.ones((400,400), dtype='uint8')
cv2.rectangle(img_rectangle, (50,50),(300,300),(255,255,255), -1) 
img_circle = np.ones((400,400), dtype='uint8')
cv2.circle(img_circle, (300,300), 70, (255,255,255), -1)


### AND
# bitwiseAnd = cv2.bitwise_and(img_rectangle, img_circle)
# cv2.imshow("image bitwiseAnd", bitwiseAnd)
# cv2.waitKey(0)

### OR
# bitwiseOr = cv2.bitwise_or(img_rectangle, img_circle)
# cv2.imshow("image bitwiseOr", bitwiseOr)
# cv2.waitKey(0)

### XOR (교집합)
# bitwiseXor = cv2.bitwise_xor(img_rectangle, img_circle)
# cv2.imshow("image bitwiseXor", bitwiseXor)
# cv2.waitKey(0)

### NOT
# rectangle기준
# bitwiseNot = cv2.bitwise_not(img_rectangle)
# cv2.imshow("rectangle Not", bitwiseNot)
# cv2.waitKey(0)


# circle기준
# bitwiseNot = cv2.bitwise_not(img_circle)
# cv2.imshow("circle Not", bitwiseNot)
# cv2.waitKey(0)


######### ex-04 마스킹 ############
mask = np.zeros((683,1024,3), dtype='uint8') # 683, 1024뒤에 3 안붙이면 흑백만 나옴(컬러가 안된다고 함.)
cv2.rectangle(mask, (60,50), (280,280), (255,255,255), -1)
cv2.rectangle(mask, (420,50), (550,230), (255,255,255), -1)
cv2.rectangle(mask, (750,50), (920,280), (255,255,255), -1) 
cv2.imshow('....', mask)
cv2.waitKey(0)

#################### 과제 ##########################
# img = cv2.imread('./face.png')
# print(img.shape)
# mask = np.zeros_like(img)
# # mask = np.zeros((300,332), dtype='uint8')
# # cv2.rectangle(mask, (60,50), (280,280), (255,255,255), -1)
# # cv2.rectangle(mask, (420,50), (550,230), (255,255,255), -1)
# # cv2.rectangle(mask, (750,50), (920,280), (255,255,255), -1)
# masked = cv2.bitwise_and(img, mask)
# cv2.imshow('....', masked)
# cv2.waitKey(0)