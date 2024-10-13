from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit
import sys


if __name__ == "__main__":
    # 1. 创建应用程序
    app = QApplication(sys.argv)

    # 2. 创建窗口
    w = QWidget()
    # 设置标题
    w.setWindowTitle("布局的嵌套")
    # w.resize(640, 480)
    # 创建水平排列的布局 水平 Horizontal  垂直 Vertical
    
    root_layout = QHBoxLayout()
    w.setLayout(root_layout)
    # 第1列
    col1_layout = QVBoxLayout()
    col1_layout.addWidget(QPushButton("1"))
    # 第2列
    col2_layout = QVBoxLayout()
    col2_layout.addWidget(QPushButton("1"))
    col2_layout.addWidget(QPushButton("2"))
    # 第3列
    col3_layout = QVBoxLayout()
    col3_layout.addWidget(QPushButton("1"))
    col3_layout.addWidget(QPushButton("2"))
    col3_layout.addWidget(QPushButton("3"))
    # 第4列
    col4_layout = QVBoxLayout()
    col4_layout.addWidget(QPushButton("1"))
    col4_layout.addWidget(QPushButton("2"))
    col4_layout.addWidget(QPushButton("3"))
    col4_layout.addWidget(QPushButton("4"))
    
    root_layout.addLayout(col1_layout)
    root_layout.addLayout(col2_layout)
    root_layout.addLayout(col3_layout)
    root_layout.addLayout(col4_layout)
    

    # 3. 显示窗口
    w.show()
    # 等待app停止
    sys.exit(app.exec_())
