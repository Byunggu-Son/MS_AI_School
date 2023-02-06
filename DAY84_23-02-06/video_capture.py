import cv2

folder_num = 36# 저장위치 폴더 숫자 지정
vidcap = cv2.VideoCapture(f'./drone_dataset/drone_video/{folder_num}/drone_video.mp4') ## 다운받은 비디오 이름

success,image = vidcap.read()
count = 0

while(vidcap.isOpened()):
    ret, image = vidcap.read()
    
    if count == 1500: # 종료 시점 
        break

    if(int(vidcap.get(1)) % 40 == 0): # 프레임당 저장 
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv2.imwrite(f"./drone_dataset/drone_video/{folder_num}/frame%d.jpg" % count, image)
        print('Saved frame%d.jpg' % count)
        count += 1