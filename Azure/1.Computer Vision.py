#!/usr/bin/env python
# coding: utf-8

# Computer Vision Object Dectection
# 
# Computer Vision API를 사용해서 이미지속에 있는 사물을 인식하는 데모 입니다.
# 
# 네트워크 통신을 위해서 requests 패키지를 import 합니다
# 
# 
# 

# In[ ]:


import requests #Azure안에 있는 것을 불러와야되니깐.


# 이미지처리를 위해서 matplotlib.pyplot, Image, BytesIO 세 개의 패키지를 import 합니다.
# 
# matplotlib.pyplot는 import 할 때 시간이 조금 걸릴 수 있습니다.

# In[ ]:


import matplotlib.pyplot as plt # AI할때 굉장히 많이 사용하는 패키지
from PIL import Image #이미지 담당하는 패키지
from io import BytesIO

import json


# Subscription Key와 접속에 필요한 URL을 설정합니다.

# In[ ]:


subscription_key = '4ea25517b01a4d7da2e268bbd168929f'
vision_base_url = 'https://labuser18computervision.cognitiveservices.azure.com/vision/v2.0/'

analyze_url = vision_base_url + 'analyze' # vision_base_url뒤에 analyze가 붙으면 이미지 분석을 위한 주소가 됨.


# 분석에 사용되는 이미지를 확인합니다.

# In[ ]:


image_url = 'https://img0.yna.co.kr/etc/inner/KR/2016/10/29/AKR20161029046000004_01_i_P2.jpg'

#con = requests.get(image_url) 200이 나오면 통신 잘되는 상태
con = requests.get(image_url).content # 자체적으로 이미지 못 가져가게 막는 사이트도 있어서 확인해야 됨.
byte = BytesIO(con) # content를 붙이면 바이너리로 가져와서 바이트 단위로 쪼개야하기 때문에

image = Image.open(byte)

# 한줄로 간편하게 쓰면 image = Image.open(BytesIO(requests.get(image_url).content))
image


# In[ ]:


headers = {'Ocp-Apim-Subscription-key': subscription_key}
params  = {'visualFeatures': 'Categories,Description,Color'} #뒤에 목록들 띄어쓰기하면 에러남.
data = {'url': image_url}


# In[ ]:


response = requests.post(analyze_url, headers = headers, params = params, json = data) #웹 호출하는 방법은 get or post


# In[ ]:


result = response.json()
result


# In[ ]:


image_caption = result['description']['captions'][0]['text'] #Description밑에 captions밑 0번째의 text를 가져오겠다. json은 대소문자 가리므로 타이핑 시 주의


# In[ ]:


image_caption


# Object Detection

# In[ ]:


objectDetection_url =  vision_base_url + 'detect' # url뒤에 detect붙이면 오브젝트 디택트를 위한 주소


# In[ ]:


image_url = 'https://mblogthumb-phinf.pstatic.net/MjAyMDA5MDdfMjQ1/MDAxNTk5NDY1MjUxMjM4.zbBfDyquP67Utlw2d6pFOtHqnJyfkukH3PTDgDTg8Zkg.qQWiX02sgIaExMrU-guWXKDRsmnGBBxeS_bz2Ioy8YUg.PNG.vet6390/%EA%B0%95%EC%95%84%EC%A7%80_%EA%B3%A0%EC%96%91%EC%9D%B4_%ED%95%A8%EA%BB%98_%ED%82%A4%EC%9A%B0%EA%B8%B0.PNG?type=w800'


# In[ ]:


image = Image.open(BytesIO(requests.get(image_url).content)) #위와 다르게 한줄 코드로 간편하게 해보자.
image


# In[ ]:


headers = {'Ocp-Apim-Subscription-key': subscription_key}
params  = {'visualFeatures': 'Categories,Description,Color'}
data = {'url': image_url}


# In[ ]:


response = requests.post(objectDetection_url, headers = headers, params = params, json = data)


# In[ ]:


result = response.json()
result #오브젝트 디택션에서는 rectangle에 해당하는 바운딩박스가 제일 중요하다. 객체 간 관계도 볼 수 있어서?


# In[ ]:


# 그림을 그릴 수 있는 라이브러리 필요.
# 텍스트로 개체에 이름을 쓸 패키지 필요.
from PIL import Image, ImageDraw, ImageFont

draw = ImageDraw.Draw(image) #위의 패키지이다.


# In[ ]:


# boundingBox를 위한 함수
def DrawBox(detectData):
  objects = detectData['objects']

  for obj in objects: #요소 수 만큼 반복됨. objects의 요소는 두개 이므로 for문은 두 번 반복.
    # print(obj) 
    #값이 잘 나오니 이제 obj안의 rectangle을 뽑아내기로하자

    rect = obj['rectangle']
    print(rect)

    x = rect['x']
    y = rect['y']
    w = rect['w']
    h = rect['h']

    draw.rectangle(((x,y),(x+w,y+h)), outline='red') #draw.rectangle이라는 명령어가 있다. 두 개의 꼭짓점이 필요한 것.


    # 이미지 안에 글자를 넣어보자
    objectName = obj['object']
    draw.text((x,y),objectName,fill='red')#draw안에 text라는 명령어가 있다


# In[ ]:


DrawBox(result)


# In[ ]:


image


# In[ ]:




