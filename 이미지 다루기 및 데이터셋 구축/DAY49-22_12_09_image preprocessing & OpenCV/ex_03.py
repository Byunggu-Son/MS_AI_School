# 셀레늄이용하여 데이터셋 결과물을 디렉토리 스크린샷, 데이터 csv로 만든 결과(학습 100장, 테스트용 20장) 스크린샷까지가 dataset class 코드까지( 최소 3종류)
# dataset class는 mnist학습 네트워크의 입력에 맞게 생성(리사이즈)
# 된다면 학습과 테스트 진행

import os
from collections import defaultdict
import random

random.seed(0)

label_dict = defaultdict(int)

data_cnt_list = []
datapath = 'C:/Users/user/Documents/Github/MS_AI_School/DAY49-22_12_09/data'
label_index = 0
for idx, v in enumerate(os.listdir(datapath)):
    label_dir = os.path.join(datapath, v)
    if os.path.isdir(label_dir):
        label_dict[v] = label_index
        label_index += 1     
        data_cnt_list.append(len(os.listdir(v)))

print(label_dict)
test_data_cnt = int(sum(data_cnt_list)/len(data_cnt_list)*0.2)
train_df_list = defaultdict(list)
test_df_list = defaultdict(list)


for i in os.listdir(datapath):
    label_path = os.path.join(datapath, i)
    if os.path.isdir(label_path):
        total_data = os.listdir(label_path)
        test_data = random.sample(total_data, test_data_cnt)
        train_data = [os.path.join(i, j) for j in test_data if j not in test_data]
        train_df_list['file name'] = train_data
        test_df_list['file name'] = [os.path.join(i, t) for t in test_data]
        train_df_list['label'] = [label_dict[i] for _ in range(len(train_data))]
        test_df_list['label'] = [label_dict[i] for _ in range(len(test_data))]

import pandas as pd
tr_df = pd.DataFrame(train_df_list)
te_df = pd.DataFrame(test_df_list)
print(tr_df.head())
print(te_df.head())
print(tr_df['label'].unique())
print(te_df['label'].unique())