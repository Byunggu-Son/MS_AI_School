import cv2
import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torchvision.io import read_image

training_data = datasets.FashionMNIST(
    root="data", 
    train=True, 
    download=True, 
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False, 
    download=True, 
    transform=ToTensor()
)

img_size = 28
num_images = 5

with open('./data/FashionMNIST/raw/t10k-images-idx3-ubyte', 'rb') as f:
    a = f.read(16)
    buf = f.read(img_size*img_size*num_images)
    data = np.frombuffer(buf, dtype=np.uint8).astype(float)
    data = data.reshape(num_images, img_size, img_size, 1)
    
    image = np.asarray(data[1]).squeeze()
    plt.imshow(image)
    plt.show()

with open('./data/FashionMNIST/raw/train-labels-idx1-ubyte', 'rb') as f:
    buf = f.read(num_images)
    labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
    print(labels[1])
    
    


labels_map = {0: 'T-Shirt',
              1: 'Trouser',
              2: 'Pullover',
              3: 'Dress',
              4: 'Coat',
              5: 'Sandal',
              6: 'Shirt',
              7: 'Sneaker',
              8: 'Bag',
              9: 'Ankle Boot'}

columns = 3
rows = 3
fig = plt.figure(figsize=(8, 8))

for i in range(1, columns * rows+1):
    sample_idx = torch.randint(len(training_data), size=(1,)).item()
    img, label = training_data[sample_idx]
    fig.add_subplot(rows, columns, i)
    plt.title(labels_map[label])
    plt.axis('off')
    plt.imshow(img.squeeze(), cmap='gray')
plt.show()



### save annotation csv
# header
imgf = open('./data/FashionMNIST/raw/train-images-idx3-ubyte', 'rb')
imgd = imgf.read(16)
lblf = open('./data/FashionMNIST/raw/train-labels-idx1-ubyte', 'rb')
lbuf = lblf.read(8)
df_dict = {
    'file_name' : [],
    'label' : []
}


idx = 0

os.makedirs('./imgs', exist_ok=True) 
while True:     
    imgd = imgf.read(img_size*img_size)
    if not imgd:
        break
    data = np.frombuffer(imgd, dtype=np.uint8).astype(float)
    data = data.reshape(1, img_size, img_size, 1)
    image = np.asarray(data).squeeze()
    lbld = lblf.read(1)
    labels = np.frombuffer(lbld, dtype=np.uint8).astype(np.int64)
    file_name = f'{idx}.png'
    cv2.imwrite(f'./imgs/{file_name}', image)
    idx += 1
    df_dict['label'].append(labels[0])
    df_dict['file_name'].append(file_name)
#print(df_dict)
df = pd.DataFrame(df_dict)
print(df)
df.to_csv('./annotations_train.csv')



################################################################
# test dataset만들기
imgf = open('./data/FashionMNIST/raw/t10k-images-idx3-ubyte', 'rb')
imgd = imgf.read(16)
lblf = open('./data/FashionMNIST/raw/t10k-labels-idx1-ubyte', 'rb')
lbuf = lblf.read(8)
df_dict = {
    'file_name' : [],
    'label' : []
}

idx = 0

os.makedirs('./imgs_2', exist_ok=True) 
while True:     
    imgd = imgf.read(img_size*img_size)
    if not imgd:
        break
    data = np.frombuffer(imgd, dtype=np.uint8).astype(float)
    data = data.reshape(1, img_size, img_size, 1)
    image = np.asarray(data).squeeze()
    lbld = lblf.read(1)
    labels = np.frombuffer(lbld, dtype=np.uint8).astype(np.int64)
    file_name = f'{idx}.png'
    cv2.imwrite(f'./imgs_2/{file_name}', image)
    idx += 1
    df_dict['label'].append(labels[0])
    df_dict['file_name'].append(file_name)
#print(df_dict)
df = pd.DataFrame(df_dict)
print(df)
df.to_csv('./annotations_test.csv')

#######################################################################




class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file, names=['file_name', 'label'], skiprows=[0])
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = read_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label
    
    
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 128)
        self.fc4 = nn.Linear(128, 64)
        self.fc5 = nn.Linear(64, 32)
        self.fc6 = nn.Linear(32, 10)
        
    def forward(self, x):
        x = x.float()
        h1 = F.relu(self.fc1(x.view(-1, 784)))
        h2 = F.relu(self.fc2(h1))
        h3 = F.relu(self.fc3(h2))
        h4 = F.relu(self.fc4(h3))
        h5 = F.relu(self.fc5(h4))
        h6 = self.fc6(h5)
        return F.log_softmax(h6, dim=1)
    
print('init model done')


epochs = 10 # 학습을 몇번할것인가?
lr = 0.01   # Learning rate : 업데이트 시킬때 한번에 어느정도 할 것인가? 
            # 적당한 러닝레이트를 찾아야한다!
momentum = 0.5 # 옵티마이저에 최적화함수에 들어가는것인데 관성이다.
               # 더 진행을 해보고 더욱 수렴하는 방향이 있는지 확인하라

no_cuda = True
seed = 1
log_interval = 200 # log_interval: 학습이 진행되면서 Mini-Batch의 Index를 이용해 과정을 모니터링할 수 있도록 출력하는 것 의미

use_cuda = not no_cuda and torch.cuda.is_available()
torch.manual_seed(seed)
device = torch.device("cuda" if use_cuda else "cpu")
kwargs = {"num_workers": 1, "pin_memory": True} if use_cuda else {}
print("set vars and device done")

# train_loader = torch.utils.data.DataLoader(
#     datasets.MNIST('.../data', train=True,
#                    download=True,transform=transform),
#     batch_size = batch_size, shuffle=True, **kwargs)


batch_size = 64
test_batch_size = 1000



train_dataset = CustomImageDataset(
    annotations_file='C:/Users/user/Documents/Github/MS_AI_School/DAY49-22_12_09/annotations_train.csv',
    img_dir='C:/Users/user/Documents/Github/MS_AI_School/DAY49-22_12_09/imgs',
)


############################################################################################

# test data set만들기

test_dataset = CustomImageDataset(
    annotations_file='C:/Users/user/Documents/Github/MS_AI_School/DAY49-22_12_09/annotations_test.csv',
    img_dir='C:/Users/user/Documents/Github/MS_AI_School/DAY49-22_12_09/imgs_2',
)


############################################################################################


train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size = test_batch_size, shuffle=True, **kwargs)

# test_loader = torch.utils.data.DataLoader(
#         datasets.MNIST('../data', train=False, download=True,
#                  transform=transform),
#     batch_size=test_batch_size, shuffle=True, **kwargs)

model = Net().to(device) # to() : 어떤한 변수나 가중치들 텐서로 이루어질수 있는 값들을 torch.device하에 보낼 수 있다. cpu 
# 옵티마이저는 로스값을 줄이는데 어디든 사용. 
optimizer = optim.SGD(model.parameters(), lr=lr, momentum=momentum)


def train(log_interval, model, device, train_loader, optimizer, epoch):
    model.train()# 모델을 train하겠다.
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)# 어떤 디바이스에 따라 연산해주겠다를 정의
        optimizer.zero_grad() # 배치 한번 돌면서 로스값 저장하고 이전 배치에 대한 것을 지우고 다음 업데이트에 대한 것을 넣어준다.
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))
 
 
     

def test(log_interval, model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += F.nll_loss(output, target, reduction='sum').item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item() # 같은 것만 카운트되서 1이 되니 그것만 더해서 맞춘 갯수 구한다.

    test_loss /= len(test_loader.dataset) # 데이터 갯수로 나눠서 로스 값의 갯수를 구한 것.

    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format
          (test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))

for epoch in range(1, 11):
    train(log_interval, model, device, train_loader, optimizer, epoch)
    test(log_interval, model, device, test_loader)
torch.save(model, './model.pt') # 가중치 담은 모델을 저장.(pt라는 확장자로 저장한다는 것을 알아두자.)
#PyTorch에서는 모델을 저장할 때 .pt 또는 .pth 확장자를 사용하는 것이 일반적인 규칙


#