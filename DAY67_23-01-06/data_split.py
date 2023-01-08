import glob
import os
import random
import shutil

import cv2

def image_size(path):
    # folder image size
    # 경로 불러오기
    AAA = glob.glob(os.path.join(path, "data","*.png"))

    # # image view
    # 경로에서 이미지 잘 불러왔는지 시각적으로 확인
    for i in AAA[:10]:
        img = cv2.imread(i)
        cv2.imshow("test",img)
        cv2.waitKey(0)
    # show print

    show_flg = False # 밑의 이미지 사이즈를 ON / OFF역할
    if show_flg == True:
        print(f"폴더명 >> {len(AAA)}")

# train / val 데이터 나누기, data폴더 -> train/val나눈 뒤 dataset으로 이동까지.
def create_train_val_split_folder(path):
    all_categoires = os.listdir(path)
    print("모든 카테고리>> ", all_categoires)

    # train / val 나누기 위한 폴더 생성
    os.makedirs("./dataset/train/", exist_ok=True)
    os.makedirs("./dataset/val/", exist_ok=True)

    # dataset/train으로 이미지 저장
    for category in sorted(all_categoires):
        # 각 라벨별 train 폴더 안에 폴더 생성
        os.makedirs(f"./dataset/train/{category}", exist_ok=True)
        all_image = os.listdir((f"./data/{category}/"))
        for image in random.sample(all_image, int(0.9 * len(all_image))): # 전체이미지에서 val추출을 위해 random.sample(컬렉션, 샘플수) 사용. 각 원래의 이미지 폴더에서90%씩 추출
            # print(image)

            # origin dataset, new dataset (shutil.move는기존경로에서 옮기고 싶은 경로로)
            shutil.move(f"./data/{category}/{image}",
                        f"./dataset/train/{category}")

    # dataset/val으로 이미지 저장
    for category in sorted(all_categoires):
        os.makedirs(f"./dataset/val/{category}", exist_ok=True)
        all_image = os.listdir((f"./data/{category}/"))
        for image in all_image: # 위의 train에서 90%를 가져갔으니 따로 나누지 않고 다 가져가면 된다.
            shutil.move(f"./data/{category}/{image}",
                        f"./dataset/val/{category}")

if __name__ == '__main__':
    path = "./data"
    # image_size(path)
    create_train_val_split_folder(path)