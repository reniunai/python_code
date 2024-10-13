from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
import sys

# 1. 创建应用程序
app = QApplication(sys.argv)

# 2. 创建窗口
w = QWidget()
# 设置标题
w.setWindowTitle("黑马窗口")
# 设置窗口大小
# w.resize(1280, 720)
# 指定位置和大小
# w.setGeometry(200, 100, 640, 480)
# 设置窗口图标
icon = QIcon("qq.png")
w.setWindowIcon(icon)
# 鼠标悬浮文字
w.setToolTip("气泡提示")

# 3. 显示窗口
w.show()

# 等待app停止
sys.exit(app.exec_())