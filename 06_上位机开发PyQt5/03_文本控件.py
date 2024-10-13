from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys

# 1. 创建应用程序
app = QApplication(sys.argv)

# 2. 创建窗口
w = QWidget()
# 设置标题
w.setWindowTitle("黑马窗口")
w.resize(640, 480)

# ---------------------------------------------------- 组件初始配置 start

label = QLabel()
label.setText("第一个文本")
# 将文本添加到窗口
label.setParent(w)

# ---------------------------------------------------- 组件初始配置 end

# 3. 显示窗口
w.show()

# 等待app停止
sys.exit(app.exec_())