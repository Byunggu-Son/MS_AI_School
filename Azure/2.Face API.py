#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


# In[3]:


subscription_key = 'efa0eed3a36a44b6b0399f2e23178f51'
face_api_url = 'https://labuser18face.cognitiveservices.azure.com/face/v1.0/detect'

image_url = 'http://image.koreatimes.com/article/2021/05/10/20210510094734601.jpg'


# In[5]:


image = Image.open(BytesIO(requests.get(image_url).content))


# In[7]:


headers = {'Ocp-Apim-Subscription-key': subscription_key}


# In[29]:


params = {
    # 'returnFaceID': 'true', #인권 문제로 FaceID와 더불어 Attributes 대부분 사용안됨.
    'returnFaceLandMarks': 'false',
    'returnFaceAttributes': 'smile'
}


# In[30]:


data = {'url': image_url}


# In[31]:


response = requests.post(face_api_url, params=params, headers=headers, json=data)
faces = response.json()
faces


# In[32]:


draw = ImageDraw.Draw(image)


# In[43]:


def DrawBox(faces):
  for face in faces:
    rect = face['faceRectangle']
    left = rect['left']
    top = rect['top']
    width = rect['width']
    height = rect['height']

    draw.rectangle(((left,top),(left+width,top+height)),outline='red')

    face_attributes = face['faceAttributes']
    smile = face_attributes['smile']

    draw.text((left,top),str(smile), fill='red') # draw가 쉽긴 하나, 글자크기나 선 굵기의 옵션은 없다..


# In[44]:


DrawBox(faces)


# In[45]:


image


# In[ ]:




