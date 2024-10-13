import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget
import sys

from ui.Ui_my_widget import Ui_MyWidget

class MyWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MyWidget()
        self.ui.setupUi(self)
        
        self.init_ui()

    # def on_btn_send_clicked(self, arg = False):
    #     print("按钮按下", arg)
    
    def on_btn_send_click(self):
        print("按钮按下")

    def init_ui(self):
        self.ui.btn_send.clicked.connect(self.on_btn_send_click)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWidget()
    w.show()

    sys.exit(app.exec_())