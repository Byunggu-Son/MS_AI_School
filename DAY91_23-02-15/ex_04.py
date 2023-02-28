## ex_04 체크 메뉴, 컨텍스트 메뉴
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, qApp
from PyQt5.QtCore import QCoreApplication

class Exam(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.initUI()

# 각 그룹, 메뉴의 위치는 헷갈리지 않도록 작성하기. ★
# 기본 틀은 맨 위에 메인 그룹, 메뉴 객체 / 서브 그룹, 서브 메뉴

    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage("안녕하세요!")

        menu = self.menuBar() # 메뉴바 생성
        menu_file = menu.addMenu('File') # 메인 그룹 생성
        menu_edit = menu.addMenu('Edit') # 메인 그룹 생성
        menu_view = menu.addMenu('View') # 메인 그룹 생성

        file_exit = QAction('Exit', self) # 메뉴 객체 생성
        file_exit.setShortcut('ctrl+Q') # 단축키 지정
        file_exit.setStatusTip('누르면 잘가고~') # 상태표시줄에 표시될 문구.
        new_txt = QAction('텍스트 파일', self)
        new_py = QAction('파이썬 파일', self)
        view_stat = QAction('상태표시줄',self, checkable=True)
        view_stat.setChecked(True)

        # file_exit.triggered.connect(QCoreApplication.instance().quit)
        file_exit.triggered.connect(qApp.quit) # 더 간편하게 끄기 가능.
        view_stat.triggered.connect(self.tglStat) # 상태표시줄 끄고 켜기.

        file_new = QMenu('New', self) # 서브 그룹 생성

        file_new.addAction(new_txt) # 서브 메뉴 생성
        file_new.addAction(new_py) # 서브 메뉴 생성

        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit) # 메뉴 등록
        menu_view.addAction(view_stat)
        self.resize(450, 400)
        self.show()
    
    def tglStat(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()
    def contextMenuEvent(self, QContextMenuEvent): # 이미 정의된 함수이므로 재정의해서 사용
        cm = QMenu(self)

        quit = cm.addAction('Quit')

        action = cm.exec_(self.mapToGlobal(QContextMenuEvent.pos())) # 전체적인 맵의 위치를 저장해서 넘김. 추후 우클릭을 어느 위치에서 했냐에 따라 다른 메뉴나올 수 있도록
        if action == quit:
            qApp.quit() # 위의 QCoreApplication보다 더 간단한 방법으로는 qApp import한 후 이렇게 적어주면 끝!


app = QApplication(sys.argv) 
w = Exam() 
sys.exit(app.exec_()) 
