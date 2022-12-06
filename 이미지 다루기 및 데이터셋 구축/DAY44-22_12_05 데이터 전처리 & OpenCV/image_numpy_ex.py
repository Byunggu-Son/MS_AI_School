import numpy as np
# pip install opencv-python==4.5.5.62
import cv2 # opencv는 최신 버전일수록 문제가 많아서 한 단계 낮추는 것을 권장

# 이미지 경로
x = cv2.imread('./cat.png', 0) # 흑백 이미지
print(x)
y = cv2.imread('./cat.png', 1) # 컬러 이미지
print(y)

cv2.imshow('cat image show gray', x)
cv2.imshow('cat image show', y)
cv2.waitKey(0) # 얘를 안써주면 이미지 불러오다가 꺼진다고 함. 써줘야 다 불러올 때까지 기다림. 이미지일때는 0, 비디오일때는 1(프레임 단위라서)


# 여러개 파일 save .npz
np.savez('./image.npz', array1=x, array2=y)

# 압축 방법
np.savez_compressed('./image_compressed.npz', array1=x, array2=y)

# npz 데이터 로드
data = np.load('./image_compressed.npz')

result1 = data['array1']
result2 = data['array2']

cv2.imshow("result01", result1)
cv2.waitKey(0)