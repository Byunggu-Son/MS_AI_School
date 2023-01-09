# 23-01-06 진행했던 webcam 테스트 코드 
import cv2
from torchvision import models
from torchvision import transforms
import torch.nn as nn
import torch

# 학습의 순서는 모델 아키텍처 -> 학습 모델 불러오기.
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 가로
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 세로

# model
net = models.resnet18(pretrained=False) # 이후 버전에서는 pretrained=False가 remove된다고 함(지금은 warning뜨고 실행.)
net.fc = nn.Linear(in_features=512, out_features=클래스개수) # 512는 resnet18의 디폴트(이건 못 바꿈)

# 학습한 모델 불러오기
# 이 과정은 꼭 알아두기!!!
models_loader_path = "./weight/resnet.pt" # 보통은 weight폴더에 pt파일을 둔다고 함.
net.load_state_dict(torch.load(models_loader_path, map_location=device)) # cuda에서 cpu로 하면 써줘야됨. cuda대 cuda일 경우는 필요없으나 이 경우는 cuda에서 cpu쓰므로.(device대신 "cpu"를 써줘도 됨)
net.to(device)

val_transforms = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])
])

def preprocess(image, device):
    from PIL import Image
    image = Image.fromarray(image)
    image = val_transforms(image)
    image = image.float()
    image = image.to(device)
    image = image.unsqueeze(0) # unsqueeze는 차원 늘려준다. 현재 3D이기에 4D를 input해야되기 때문에.(보통 어느 모델이든 unsqueeze(0)를 쓰나 확인위해 밑에서 size찍어봄.).
    # reshape도 가능하나 안에 들어갈 내용들을 해야하기에 더 간편한 unsqueeze(0)를 쓴다.

    # print(image.size())
    return image

if not webcam.isOpened():
    print("카메라 열기 실패 !!!")
    exit()

while webcam.isOpened():
    status, frame = webcam.read()
    frame = cv2.flip(frame, 1) # 좌우 대칭
    
    net.eval() # net.eval()과 with torch.no_grad()는 짝꿍. 더 이상 학습하지 않겠다 의미.
    with torch.no_grad():
        if status:
            image = preprocess(frame, device)
            output = net(image)
            print("output", output)
            _, argmax = torch.max(output,1)
            print("argmax", argmax)
            cv2.imshow("test", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
webcam.release()
cv2.destroyAllWindows()