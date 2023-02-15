## ex_01 pyqt5 기본 공부하기

# 기본적으로 가져와야되는 것들
import sys # 시스템, 셀, 스크립트 정보
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton  #Qtwidgets 대부분의 위젯들 포함, 기본적으로 QApplication, Qwidget은 무조건 불러온다고 생각, 대부분 Q로 시작함.

# 클래스는 QWidget을 상속받아서 생성
# 나만의 창을 만들 클래스, 위젯에서 상속을 받아서 만듬. 

class Exam(QWidget): 
    def __init__(self):

        #Qwidget에 해당하는 상위 객체 생성
        super().__init__()
        self.initUI() # 밑에서 만들 것

    def initUI(self):
        btn = QPushButton('Q푸쉬버튼', self) # 나 자신한테 버튼 추가.
        btn.resize(btn.sizeHint()) # sizeHint : 글씨를 기준으로 적당하게 크기를 조절해준다.
        btn.setToolTip('툴팁이고요 <b> 반갑다고.</b>') # 마우스 가져다대면 뜨는 박스. html태그까지 가능.
        btn.move(20, 30) # 버튼 위치 이동

        self.setGeometry(300,300,400,500 ) # 창 위치 및 크기 조절. 창의 위치를 모니터 좌상단으로부터 가로 300px, 세로300px, 창의 크기를 가로 400px, 세로 500px
        self.setWindowTitle('첫 번째 학습시간')
        self.show()

# 모든 Qt5 어플리케이션은 반드시 어플리케이션 오브젝트를 생성해야됨. 밑은 어플리케이션 생성 단계

app = QApplication(sys.argv) # sys.argv : 파이썬이 쉘 스크립트에서 실행할 때 명령 줄로 인수를 받을 수 있는데 그 부분을 제어. 본 강좌에선 f10으로 진행하니 이런 기능있구나~정도로 생각

w = Exam() # 클래스 이름을 따옴. 내가 만든 창이 들어갈 객체를 만듬.

sys.exit(app.exec_()) # 프로그램을 깨끗히 종료한다! app.exec()는 파이썬에서 쓰이는 키워드라 밑에 _언더바 추가. 

# app.exec_()는 이벤트(클릭, 드래그, 엔터 등등) 처리를 위한 루프 실행. app.exec_()가 계속 돌아가다가 메인 루프가 끝났을 때(창 종료,exit내부에서 exit함수를 실행한다던지 등등) exit가 실행.

# 코드 실행 결과 위젯창이 실행된다! 위젯창 vs 일반창의 차이는 메뉴가 없다.

