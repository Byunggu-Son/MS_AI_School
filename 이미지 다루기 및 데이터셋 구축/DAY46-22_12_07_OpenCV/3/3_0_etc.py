from PIL import Image
import cv2

'''
opencv -> np array : bgr
Image -> pil : rgb
'''

img = cv2.imread('./Billiards.png')
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
pil_img = Image.fromarray(rgb_img)
pil_img.show()

# pil의 장점 : binary이미지 읽을 수 있음, 메타데이터를 다룰 수 있다.