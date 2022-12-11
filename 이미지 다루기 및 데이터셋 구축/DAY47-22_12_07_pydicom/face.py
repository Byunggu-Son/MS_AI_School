import cv2
import numpy as np

# Creating face_cascade and eye_cascade objects
# 얼굴과 눈을 잡는 cascade 각각 생성
face_casacade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_casacade = cv2.CascadeClassifier('./haarcascade_eye.xml')

###############################

# 이미지 불러오기
img = cv2.imread('./face.png')
# print(img.shape) # 이미지 크기를 체크
# cv2.imshow('image show', img)
# cv2.waitKey(0)

###############################

# 이미지를 그레이 스케일로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_casacade.detectMultiScale(gray, 1.1, 4) # 받는 인자갯수 / x, y ,w, h가 나오게 하려면 4개

###############################

# 얼굴 이미지에 그릴 직사각형 정의 및 드로잉
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0), 2) # 좌표값(w,h값을 더해 직사각형 그릴 좌표얻음. 쉽게는 드래그 생각), 색상, 굵기
# cv2.imshow('face', img)
# cv2.waitKey(0)    
    
###############################

# 직사각형 안 2개의 관심 영역 생성 (눈)
roi_gray = gray[y:y+h, x:x+w]
roi_color = img[y:y+h, x:x+w] 

#################################

# 두 눈 변수 생성
eyes = eye_casacade.detectMultiScale(roi_gray, 1.1, 4) # roi_gray로 전체 이미지가 아닌 얼굴 이미지를 주면 됨. 바운딩박스안에있는 얼굴에만 gray_scale 줌
# cv2.imshow('face', roi_gray) # 잘린 영역 확인
# cv2.imshow('face', roi_color) # 위와 동일
# print(eyes) # 양 쪽 눈에 대한 좌표값이 나옴.

index=0 # 밑의 for문에서 양 쪽 눈에 대한 좌표 각각 저장 위해 생성.

######################################

# for문으로 양 쪽 눈 데이터 생성
for (ex, ey, ew, eh) in eyes:
    if index == 0:
        eye_1 = (ex, ey, ew, eh)
    elif index ==1:
        eye_2 = (ex, ey, ew, eh)
    cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (255,50,0), 2)
    index = index + 1     
# cv2.imshow('face', img)
# cv2.waitKey(0) 

########################################

# 왼쪽, 오른쪽 눈 지정
if eye_1[0] < eye_2[0]:
    left_eye = eye_1
    right_eye = eye_2
else:
    left_eye = eye_2
    right_eye = eye_1
    
#########################################

# 직사각형 중심점 좌표 계산
# 중심점 구하는 것을 dectation 쪽에서는 굉장히 많이 쓰인다고 한다!

left_eye_center = (int(left_eye[0] + (left_eye[2] / 2)), int(left_eye[1] + (left_eye[3] / 2)))
# print(left_eye_center)
left_eye_x = left_eye_center[0]
left_eye_y = left_eye_center[1]

right_eye_center = (int(right_eye[0] + (right_eye[2] / 2)), int(right_eye[1] + (right_eye[3] / 2)))
# print(right_eye_center)
right_eye_x = right_eye_center[0]
right_eye_y = right_eye_center[1]


#########################################

# 두 눈의 중심선 사이에 선 긋기
cv2.circle(roi_color, left_eye_center, 5, (255, 0, 0), -1)
cv2.circle(roi_color, right_eye_center, 5, (255, 0, 0), -1)
cv2.line(roi_color, right_eye_center, left_eye_center, (0,200,200), 1)
# cv2.imshow('face', img)
# cv2.waitKey(0)

###########################################

# 이미지 회전을 위한 수평선과 두 눈 중심점 연결하는 선 사이 각도 계산
if left_eye_y > right_eye_y:
    A = (right_eye_x, left_eye_y)
    direction = -1     # -1은 시계 방향으로 회전
else:
    A = (left_eye_x, right_eye_y)
    direction = 1
cv2.circle(roi_color, A, 5, (255,0,0), -1)
# cv2.imshow('face', img)
# cv2.waitKey(0)    
cv2.line(roi_color, right_eye_center, left_eye_center, (0,200,200), 1) # 선긋기
cv2.line(roi_color, left_eye_center, A, (0,200,200), 1) # 선긋기
cv2.line(roi_color, right_eye_center, A, (0,200,200), 1) # 선긋기
# cv2.imshow('face', img)
# cv2.waitKey(0)    
##########################################

#각도 단위는 라디안이라는 것에 유의! 
# np.arctan = 함수 단위는 라디안 단위
# 라디안 단위 -> 각도 : (Theta * 180) / np.pi

delta_x = right_eye_x - left_eye_x
delta_y = right_eye_y - left_eye_y
angle = np.arctan(delta_y/delta_x)
angle = (angle * 180) / np.pi
print(angle)
# 결과 -> -21.80140948635181 각도

h, w = img.shape[:2]

center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, (angle), 1.0)
rotated = cv2.warpAffine(img, M, (w,h))


cv2.imshow('face', rotated)
cv2.waitKey(0)