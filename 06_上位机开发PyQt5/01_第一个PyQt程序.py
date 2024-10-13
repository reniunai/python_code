from PyQt5.QtWidgets import QApplication,QWidget
import sys

# 1.创建应用程序
app = QApplication(sys.argv)

# 2.创建窗口
w = QWidget()

# 4.等待窗口停止
sys.exit(app.exec())
# 3.显示窗口
w.show()
