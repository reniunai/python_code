from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit
import sys

def on_submit():
    print("用户名：", edit_usr.text())
    print("密码：", edit_pwd.text())
    print("手机号：", edit_phone.text())

if __name__ == "__main__":
    # 1. 创建应用程序
    app = QApplication(sys.argv)

    # 2. 创建窗口
    w = QWidget()
    # 设置标题
    w.setWindowTitle("表单布局")
    # w.resize(640, 480)
        # 创建水平排列的布局 水平 Horizontal  垂直 Vertical
    layout = QFormLayout(w)
    # w.setLayout(layout)

    edit_usr = QLineEdit()    
    edit_pwd = QLineEdit()
    edit_pwd.setEchoMode(QLineEdit.Password)
    edit_phone = QLineEdit()
    # 提交按钮
    btn = QPushButton("提交")
    btn.clicked.connect(on_submit)    
    
    layout.addRow("用户名：", edit_usr)
    layout.addRow("密码：", edit_pwd)
    layout.addRow("手机号：",edit_phone)
    layout.addRow(btn)

    # 3. 显示窗口
    w.show()
    # 等待app停止
    sys.exit(app.exec_())
