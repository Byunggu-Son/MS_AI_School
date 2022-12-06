import cv2
import numpy as np
import matplotlib.pyplot as plt

# image loading and input image -> graysacle

img = cv2.imread('./Billiards.png', cv2.IMREAD_GRAYSCALE)

# 임계값 연산자의 출력을 마스크라는 변수에 저장
# 230보다 작으면 모든 값은 흰색 처리 / 230보다 큰 모든 값은 검은색이 됩니다.
_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)

titles = ['image','mask'] # 여기선 set_tilte이 아닌 다른 방법을 활용함
images = [img, mask]

for i in range(2): # 나오는 값이 img와 mask 두개 뿐.
    plt.subplot(1, 2, i+1),
    plt.imshow(images[i], 'gray'),
    plt.title(titles[i]),
    plt.xticks([]),
    plt.yticks([]), # for문 안에서 plt마다 ,는 구분을 위한 것. 없어도 작동 됨. 갠취인듯
plt.show()