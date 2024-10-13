import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys

class MyWidget(QWidget):
    
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(640, 480)
        
        self.init_ui()

    def on_btn_click(self):
        print("按钮按下")

    def init_ui(self):
        btn = QPushButton("按钮", self)
        btn.clicked.connect(self.on_btn_click)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWidget("窗口标题")
    w.show()

    sys.exit(app.exec_())