#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install azure-cognitiveservices-vision-customvision')


# In[2]:


# 이 프로젝트는 패키지 불러오는게 반 이상 인듯
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid


# In[3]:


ENDPOINT = 'https://labuser18custom.cognitiveservices.azure.com/'

training_key = '7921e66ac6074a62b1731f059c48a138' #리소스그룹에서 두가지중 predit안써져있는 애의 키값이다.
prediction_key = '05c1b1dc9fe848f78e57be3f7a002437'
prediction_resource_id = '/subscriptions/7ae06d59-97e1-4a36-bbfe-efb081b9b03b/resourceGroups/RG18/providers/Microsoft.CognitiveServices/accounts/labuser18custom'


# In[15]:


publish_iteration_name = 'classifyModel' #반복하는 것 : iteration

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key}) # 업데이트 되면서 credential key를 사용해 보완을 더 높인듯
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)


# In[16]:


print("Creating project...")
project = trainer.create_project("Labuser18 Project") #customvision.ai 사이트에서 코드로 프로젝트 폴더를 생성하는 것.(이전과 달리 수동이 아닌 코드로!)


# In[17]:


Jjajangmyeon_tag = trainer.create_tag(project.id, "Jjajangmyeton")
Champon_tag = trainer.create_tag(project.id, "Champon")
Tangsuyug_tag = trainer.create_tag(project.id, "Tangsuyug")


# In[18]:


import time


# In[19]:


print("Training...")
iteration = trainer.train_project(project.id)
# 훈련 시간이 오래 걸리니깐 현재 상태가 어떤지 알 수 있게 반복문 써줌
while (iteration.status != 'Completed'):
  iteration = trainer.get_iteration(project.id, iteration.id)
  print('Training status' + iteration.status)

  time.sleep(2)
print('Done!')


# In[ ]:



