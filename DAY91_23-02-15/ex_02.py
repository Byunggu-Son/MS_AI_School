##  ex_02 이벤트 처리, 메세지 박스
import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton , QMessageBox
from PyQt5.QtCore import QCoreApplication # 슬롯 수행하는 것
class Exam(QWidget): 
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton("Push", self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.clicked.connect(QCoreApplication.instance().quit) # 슬롯이랑 연결해야되니 connect, 버튼이 클릭됐을 때 연결될 슬롯이 뭐냐 그런 의미. 괄호 안에다가 해당 슬롯을 적어주면 됨. 
        # QCoreApplication이 모든 이벤트 처리를 하는 것. instance를 생성하고 quit메소드와 cliked시그널이 연결이 되었다.
        self.resize(500,500)
        self.setWindowTitle("두 번째 시간")
        self.show()


    def closeEvent(self, QCloseEvent): # 오버라이딩 메소드
        ans = QMessageBox.question(self, "종료 확인","종료하시겠습니까?",
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No) # 종료 확인 창 떴을 때 디폴트가 No로 설정(테두리 음영처리). 바꾸고 싶다면 맨 뒤에 q메세지 박스를 yes로 하면 됨.

        # 위의 q메시지는 내가 입력한 값을 다른 사람한테 건네어줄 수 있다. yes와 no라는 상수를 다른데 건넬 수가 있다. 아래와 같은 방식이 가능.

        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

app = QApplication(sys.argv) 
w = Exam() 
sys.exit(app.exec_()) 


# pyqt의 이벤트는 signal과 slot이라 생각( ex) push버튼 클릭시 클릭했다는 신호 -> 이걸 클릭했을 때 수행하는 것을 슬롯.(pyqt의 슬롯이나 파이썬 코드 등) 