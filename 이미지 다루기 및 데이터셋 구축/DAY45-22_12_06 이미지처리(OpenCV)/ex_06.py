import cv2
from utils import image_show

# 이미지 경로
image_path = './cat.jpg'

# 이미지 읽기
image = cv2.imread(image_path)

# 이미지 좌우 및 상하 반전
# 1 좌우 반전 0 상하 반전
dst_tmep1 = cv2.flip(image, 1)
dst_tmep2 = cv2.flip(image, 0)
cv2.imshow("dst_tmep1",dst_tmep1)
cv2.imshow("dst_tmep2",dst_tmep2) #cv2에서는 한글처리가 안됨
cv2.waitKey(0)


# # 이미지 회전
# img90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE) # 시계 방향으로 90도 회전
# img180 = cv2.rotate(image, cv2.ROTATE_180) # 180도 회전
# img270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE) # 반시계로 돌렸을 땐 270도니깐.

# cv2.imshow("original image", image)
# cv2.imshow("rotate90", img90)
# cv2.imshow("rotate180", img180)
# cv2.imshow("rotate270", img270)

# cv2.waitKey(0)
