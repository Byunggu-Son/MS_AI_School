import cv2


def image_show(image) :
    cv2.imshow("show", image)
    cv2.waitKey(0)
    
image_path = './cat.jpg'

# 이미지 읽기
image = cv2.imread(image_path)

# 이미지 크롭 [시작 : 끝 : 단계]
image_crop = image[40:, :430]

# 저장코드 추가 png 파일 저장
cv2.imwrite('./cat_image_40x430.png', image_crop)
image_show(image_crop)

