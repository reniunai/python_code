from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys


def init_widget(w: QWidget):
    label = QLabel()
    pixmap = QPixmap("./img.png")
    label.setPixmap(pixmap)
    
    # 将文本添加到窗口
    label.setParent(w)
    # 根据图片大小修改窗口尺寸
    w.resize(pixmap.width(), pixmap.height())


if __name__ == "__main__":
    # 1. 创建应用程序
    app = QApplication(sys.argv)

    # 2. 创建窗口
    w = QWidget()
    # 设置标题
    w.setWindowTitle("黑马窗口")
    # w.resize(640, 480)

    init_widget(w)

    # 3. 显示窗口
    w.show()

    # 等待app停止
    sys.exit(app.exec_())
