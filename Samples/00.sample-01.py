from audioop import mul
import random

random_number = random.randint(1,100)

# print(random_number)

# 숫자를 맞추는 게임. 틀릴때마다 game_count가 올라감.

game_count = 1

while True:
    try: 
    
        my_number = int(input("1-100 사이의 숫자를 입력하세요. "))

    #   입력한 숫자보다 크거나 작을 경우 알려준다.
        if my_number > random_number:
            print("Down!!")
        elif my_number < random_number:
            print("Up!!")
        else:
            print(f"축하합니다. {game_count} 만에 맞추셨습니다.")
            # print("축하합니다. {} 만에 맞추셨습니다.".format(game_count))

            break
        game_count = game_count + 1
    except:
        print('숫자만 입력해주세요!!') #예외처리를 통해 숫자 외에는 경고문.


    
    