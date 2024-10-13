from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QPushButton
import sys

# 槽函数 slot 
@pyqtSlot()
def btn_clicked():
    print("按下按钮了，火箭发射！")

def init_widget(w: QWidget):
    # 创建垂直排列的布局Vertical
    layout = QVBoxLayout()
    
    btn = QPushButton()
    btn.setText("发射1")
    # 1. 给按钮添加/关联点击事件（函数）
    btn.clicked.connect(btn_clicked)
    # 2. 关联lambda表达式（无名函数）
    # btn.clicked.connect(lambda: print("aaabbbcc"))
    # 3. 关联系统已有系统函数 
    # btn.clicked.connect(QApplication.quit)
    
    layout.addWidget(btn)
    
    w.setLayout(layout)

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
