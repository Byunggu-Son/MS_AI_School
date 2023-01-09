import copy
import os.path
import time

import torch
import torchvision
from customdata import my_customdata
import albumentations as A
from albumentations.pytorch.transforms import ToTensorV2
from torch.utils.data import DataLoader
import torch.nn as nn
from timm.loss import LabelSmoothingCrossEntropy

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

test_transforms = A.Compose([
    A.SmallestMaxSize(max_size=224),
    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.255)),
    ToTensorV2()
])
## dataset과 dataloader는 한세트다.
# dataset

test_dataset = my_customdata("./dataset/test/", transform=test_transforms)

test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False,)

### facebookresearch/deit:main','deit_tiny_patch16_224 모델##########
model = torch.hub.load('facebookresearch/deit:main',
                       'deit_tiny_patch16_224', pretrained=False) # 학습때는 True였지만 마지막 test때는 False로 바꿈
model.head = nn.Linear(in_features=192, out_features=100)
model.to(device)
######################################################################

####### resnet50 ##################################################
# model = torchvision.models.resnet50(pretrained=False) # 마지막 test때는 False로 바꿈
# model.fc = torch.nn.Linear(in_features=2048, out_features=100)
# model.to(device)
######################################################################

####### best_shufflenet_v2_x0_5 ##################################################
# model = torchvision.models.shufflenet_v2_x0_5(pretrained=False) # 마지막 test때는 False로 바꿈
# model.fc = torch.nn.Linear(in_features=1024, out_features=100)
# model.to(device)
###############################################################

criterion = LabelSmoothingCrossEntropy()



optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

def test(model, test_loader, device):
    model.load_state_dict(torch.load("./best_facebook.pt"))
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for i, (image, labels) in enumerate(test_loader):
            image, labels = image.to(device), labels.to(device)
            output = model(image)
            _, argmax = torch.max(output, 1)
            total += image.size(0)
            correct += (labels == argmax).sum().item()

        acc = correct / total * 100
        print("acc for {} image : {:.3f}%".format(total, acc))
    
if __name__ == "__main__" :
    model.load_state_dict(torch.load("./best_resnet50.pt", map_location=device))
    test(model, test_loader, device)