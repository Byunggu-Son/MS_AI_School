import torch
import os
import glob
from torch.utils.data import Dataset
import cv2


class CustomDataset(Dataset):

    def __init__(self, path, transform=None):
        self.path_all = glob.glob(os.path.join(path,"*","*.png"))
        self.transform = transform
        self.label_dict={"p":0,
                        "r":1,
                        "s":2}

    def __getitem__(self, item):
        img_path = self.path_all[item]

        print(img_path)
        folder_name = img_path.split('\\')[1]
        label = self.label_dict[folder_name]

        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        if self.transform is not None:
            image = self.transform(image=image)['image']

        return image, label

    def __len__(self):
        return len(self.path_all)

if __name__ == '__main__':
    test = CustomDataset('./dataset/train/', transform=None)
    for i in test:
        print(i)