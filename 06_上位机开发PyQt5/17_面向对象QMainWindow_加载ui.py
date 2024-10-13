import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from qt_material import apply_stylesheet
from qt_material import list_themes

from ui.Ui_my_main_window import Ui_MyMainWindow

class MyMainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MyMainWindow()
        self.ui.setupUi(self)
        
        self.counter = 0
        self.init_ui()

    def on_click(self):
        self.statusBar().showMessage(f"按钮按下了{self.counter}")
        self.counter += 1
        
    def on_refresh(self):
        print("refresh!")

    def init_ui(self):
        self.ui.pushButton_3.clicked.connect(self.on_click)
        
        self.ui.actionExit.triggered.connect(QApplication.quit)
        self.ui.actionRefresh.triggered.connect(self.on_refresh)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyMainWindow()
    
    # setup stylesheet
    apply_stylesheet(app, theme='light_pink.xml')
    
    list_themes()

    w.show()

    sys.exit(app.exec_())