from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QMessageBox
import sys

def on_delete_click():
    print("弹出删除确认对话框！")
    # QMessageBox.information(w, "删除通知", "删除该联系人将无法恢复！" )
    result = QMessageBox.question(
        w, "提示", "确认删除吗？", 
        buttons=QMessageBox.Yes | QMessageBox.Cancel, 
        defaultButton=QMessageBox.Yes
    )
    if result == QMessageBox.Yes:
        print("删除用户")
    else:
        print("取消")

if __name__ == "__main__":
    # 1. 创建应用程序
    app = QApplication(sys.argv)

    # 2. 创建窗口
    w = QWidget()
    # 设置标题
    w.setWindowTitle("布局的嵌套")
    w.resize(640, 480)
    # 创建水平排列的布局 水平 Horizontal  垂直 Vertical
    
    root_layout = QVBoxLayout(w)
    btn = QPushButton("删除用户")
    btn.clicked.connect(on_delete_click)
    root_layout.addWidget(btn)

    # 3. 显示窗口
    w.show()
    # 等待app停止
    sys.exit(app.exec_())
