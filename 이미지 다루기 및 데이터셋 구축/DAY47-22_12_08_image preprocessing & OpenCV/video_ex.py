import cv2

################# 동영상 속성 확인 ######################
cap = cv2.VideoCapture('./video01.mp4')

# 비디오 크기와 프레임 확인
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)

# print('width : ',width, 'height : ',height)
'''결과 : width :  1280.0 height :  720.0'''
# print('frame_count : ', frame_count, 'fps : ', fps)
'''결과 :  frame_count :  323.0 fps :  25.0 '''

################# 동영상 파일 읽기 ##########################
if cap.isOpened(): # 캡처 객체 초기화 확인
    while True:
        ret, frame = cap.read() # ret은 잘 읽어졌는지 T,F
        if ret :
            cv2.imshow('video file show', frame)
            cv2.waitKey(25)
        else:
            break
else: 
    print('비디오 파일 읽기 실패')
    
#리소스를 먹고 있기 때문에 리소스 반납.
cap.release()
cv2.destroyAllWindows()

