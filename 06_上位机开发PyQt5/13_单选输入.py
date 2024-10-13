from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QRadioButton, QButtonGroup
import sys

def on_group_toggle(btn: QRadioButton):
    print(btn.text(), btn.isChecked())

def on_btn_click():
    print("女：click")

if __name__ == "__main__":
    # 1. 创建应用程序
    app = QApplication(sys.argv)

    # 2. 创建窗口
    w = QWidget()
    # 设置标题
    w.setWindowTitle("对话框")
    w.resize(200, 120)
    # 创建水平排列的布局 水平 Horizontal  垂直 Vertical
    
    root_layout = QVBoxLayout(w)

    btn1 = QRadioButton("男")
    btn2 = QRadioButton("女")
    btn1.setChecked(True) # 默认选中第一个
    # btn2.clicked.connect(on_btn_click)
    
    # 把两个单选按钮添加到QButtonGroup,给group添加toggle事件
    group = QButtonGroup()
    group.addButton(btn1)
    group.addButton(btn2)
    group.buttonToggled.connect(on_group_toggle)

    root_layout.addWidget(btn1)
    root_layout.addWidget(btn2)

    # 3. 显示窗口
    w.show()
    # 等待app停止
    sys.exit(app.exec_())
