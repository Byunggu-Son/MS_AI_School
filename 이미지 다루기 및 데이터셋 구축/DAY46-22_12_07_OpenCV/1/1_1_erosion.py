import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./Billiards.png", cv2.IMREAD_GRAYSCALE)

_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)

# 커널 모양
kernel = []
for i in [cv2.MORPH_RECT, cv2.MORPH_CROSS, cv2.MORPH_ELLIPSE]: # 직사각형 커널, 십자가형 커널, 타원형 커널
    kernel.append(cv2.getStructuringElement(i, (11,11)))

# print(kernel[2]) # 위의 커널들을 확인할 수 있다.

title = ['Rectangle','Cross','Ellipse']
# kernel = np.ones((3,3), np.unit)

plt.subplot(2,2,1) # plt.imshow해도 되지만 한번에 다 보여주기 위해 subplot사용
plt.imshow(mask, 'gray')
plt.title('origin')


for i in range(3):
    erosion = cv2.erode(mask, kernel[0])
    plt.subplot(2,2,i+2)
    plt.imshow(erosion, 'gray')
    plt.title(title[i])
    plt.axis('off')
plt.show()


