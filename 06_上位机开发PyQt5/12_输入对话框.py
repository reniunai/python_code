from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QInputDialog, QFileDialog
import sys

def on_btn_click():
    text, confirm = QInputDialog.getText(w, "请输入内容", "输入10个字符以内的用户名")
    print("result: ", text, confirm)

if __name__ == "__main__":
    # 1. 创建应用程序
    app = QApplication(sys.argv)

    # 2. 创建窗口
    w = QWidget()
    # 设置标题
    w.setWindowTitle("对话框")
    w.resize(640, 480)
    # 创建水平排列的布局 水平 Horizontal  垂直 Vertical
    
    root_layout = QVBoxLayout(w)
    btn = QPushButton("创建")
    btn.clicked.connect(on_btn_click)
    root_layout.addWidget(btn)

    # 3. 显示窗口
    w.show()
    # 等待app停止
    sys.exit(app.exec_())
