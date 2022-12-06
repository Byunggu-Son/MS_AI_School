import cv2

img_path = "./cat.png"
img = cv2.imread(img_path)

print("이미지 타입 : ", type(img))
print("이미지 크기 : ", img.shape)

h, w, _ = img.shape # 보통은 이렇게 많이 쓴다고 한다.

print(f"이미지 높이 {h}, 이미지 넓이 {w}")
"""
이미지 타입 :  <class 'numpy.ndarray'>
이미지 크기 :  (399, 600, 3) (H, W, C)
"""

cv2.imshow("image show", img)
cv2.waitKey(0)
