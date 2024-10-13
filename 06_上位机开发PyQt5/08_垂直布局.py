from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QPushButton
import sys

# 槽函数 slot 
# @pyqtSlot()
# def btn_clicked():
#     print("按下按钮了，火箭发射！")

def init_widget(w: QWidget):
    # 创建水平排列的布局 水平 Horizontal  垂直 Vertical
    layout = QVBoxLayout()
    w.setLayout(layout)
    
    btn1 = QPushButton("按钮1")
    btn2 = QPushButton("按钮2")
    btn3 = QPushButton("按钮3")
    btn4 = QPushButton("按钮4")
    
    layout.addWidget(btn1)
    layout.addWidget(btn2)
    layout.addWidget(btn3)
    layout.addWidget(btn4)
    

if __name__ == "__main__":
    # 1. 创建应用程序
    app = QApplication(sys.argv)

    # 2. 创建窗口
    w = QWidget()
    # 设置标题
    w.setWindowTitle("按钮")
    # w.resize(640, 480)
    init_widget(w)

    # 3. 显示窗口
    w.show()
    # 等待app停止
    sys.exit(app.exec_())
