## ex_03 메뉴바, 상태표시줄
# 메뉴바와 상태표시줄은 위젯창에선 불가. 메인 윈도우를 이용해서 작업.
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
from PyQt5.QtCore import QCoreApplication

class Exam(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.initUI()


# 각 그룹, 메뉴의 위치는 헷갈리지 않도록 작성하기. ★
# 기본 틀은 맨 위에 메인 그룹, 메뉴 객체 / 서브 그룹, 서브 메뉴

    def initUI(self):
        self.statusBar() # 상태표시줄 추가. 최초 입력시 상태표시줄 생성 -> 한번 더 호출 시 상태표시줄 객체를 받아옴.
        self.statusBar().showMessage("안녕하세요!")

        menu = self.menuBar() # 메뉴바 생성
        menu_file = menu.addMenu('File') # 메인 그룹 생성
        menu_edit = menu.addMenu('Edit') # 메인 그룹 생성

        file_exit = QAction('Exit', self) # 메뉴 객체 생성
        file_exit.setShortcut('ctrl+Q') # 단축키 지정
        file_exit.setStatusTip('누르면 잘가고~') # 상태표시줄에 표시될 문구.
        new_txt = QAction('텍스트 파일', self)
        new_py = QAction('파이썬 파일', self)

        file_exit.triggered.connect(QCoreApplication.instance().quit)

        file_new = QMenu('New', self) # 서브 그룹 생성

        file_new.addAction(new_txt) # 서브 메뉴 생성
        file_new.addAction(new_py) # 서브 메뉴 생성

        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit) # 메뉴 등록
        self.resize(450, 400)
        self.show()


app = QApplication(sys.argv) 
w = Exam() 
sys.exit(app.exec_()) 
