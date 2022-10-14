# QR생성해주는 코드
from asyncore import read
import qrcode 

qr_data = 'www.naver.com'
qr_image = qrcode.make(qr_data)

qr_image.save(qr_data + '.png')


# txt파일에서 써진 url로 QR코드 만들기
with open('site_list.txt','rt',encoding='UTF8') as f:# with는 블럭으로 파일들을 불러와서 블럭이 자동으로 닫아주기에, 실수를 미연에 방지
    read_lines = f.readlines() #라인 단위로 읽음

    for line in read_lines:
        line = line.strip() #strip으로 문자 외에 정리
        print(line)

        qr_data = line
        qr_image = qrcode.make(qr_data)

        qr_image.save(qr_data + '.png')
        