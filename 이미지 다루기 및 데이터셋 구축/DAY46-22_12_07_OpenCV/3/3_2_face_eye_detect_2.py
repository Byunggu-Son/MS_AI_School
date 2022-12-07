import cv2
import numpy as np

face_casacade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_casacade = cv2.CascadeClassifier('./haarcascade_eye.xml')


# 얼굴 이미지 데이터
img = cv2.imread('face01.png')

# 이미지 바운딩 박스
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_casacade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
    

# 관심 영역 두개 생성
roi_color = img[y:y+h, x:x+w] 
roi_gray = gray[y:y+h, x:x+w]

# 두 눈 변수 생성
# 오른쪽 눈이 범위에 들어오지 않아 파라미터값을 기존 1.1 -> 1.3으로 수정
eyes = eye_casacade.detectMultiScale(roi_gray, 1.3, 4) 
index=0

# for문으로 양 쪽 눈 데이터 생성
for (ex, ey, ew, eh) in eyes:
    if index == 0:
        eye_1 = (ex, ey, ew, eh)
    elif index ==1:
        eye_2 = (ex, ey, ew, eh)
        
    cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,0,255), 3)
    index = index + 1


# 왼쪽, 오른쪽 눈 지정
if eye_1[0] < eye_2[0]:
    left_eye = eye_1
    right_eye = eye_2
else:
    left_eye = eye_2
    right_eye = eye_1



# 직사각형 중심점 좌표 계산
left_eye_center = (int(left_eye[0] + (left_eye[2] / 2)), int(left_eye[1] + (left_eye[3] / 2)))
left_eye_x = left_eye_center[0]
left_eye_y = left_eye_center[1]

right_eye_center = (int(right_eye[0] + (right_eye[2] / 2)), int(right_eye[1] + (right_eye[3] / 2)))
right_eye_x = right_eye_center[0]
right_eye_y = right_eye_center[1]


# 두 눈의 중심선 사이에 선 긋기
# cv2.circle(roi_color, left_eye_center, 5, (255, 0, 0), -1)
# cv2.circle(roi_color, right_eye_center, 5, (255, 0, 0), -1)
# cv2.line(roi_color, right_eye_center, left_eye_center, (0,200,200), 3)
# cv2.imshow('face01', img)
# cv2.waitKey(0)

# 이미지 회전을 위한 수평선과 두 눈 중심점 연결하는 선 사이 각도 계산
if left_eye_y > right_eye_y:
    A = (right_eye_x, left_eye_y)
    # -1은 시계 방향으로 회전
    # direction = -1
else:
    A = (left_eye_x, right_eye_y)
    # direction = -1

# 두 눈 사이 점들 잇기

# cv2.circle(roi_color, A, 5, (255,0,0), -1)

# cv2.line(roi_color, right_eye_center, left_eye_center, (0,200,200), 3)
# cv2.line(roi_color, left_eye_center, A, (0,200,200), 3)
# cv2.line(roi_color, right_eye_center, A, (0,200,200), 3)

# cv2.imshow('face01', img)
# cv2.waitKey(0)

# 왼쪽 눈 y좌표 > 오른쪽 눈 y좌표 -> 이미지를 시계방향으로 회전 반대의 경우 반시계 방향 회전
delta_x = right_eye_x - left_eye_x
delta_y = right_eye_y - left_eye_y
angle = np.arctan(delta_y/delta_x)
angle = (angle * 180) / np.pi

# 이미지를 세타만큼 회전
h, w = img.shape[:2]
center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, (angle), 1.0)
rotated = cv2.warpAffine(img, M, (w,h))

cv2.imshow("face01.png", rotated)
cv2.waitKey(0)
