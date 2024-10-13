from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QCheckBox, QLabel
import sys

def btn_state_update(arg):
    # print("抽烟：", arg)
    btn_state_update_func(0, "抽烟", arg)
    
def btn_state_update_func(flag, text, arg):
    """统一处理函数
    
    :param flag: 用于区分按钮的数字
    :param text: 可选文本描述
    :param arg: 选中状态 2选中 0未选中
    """
    print(f"{flag}:{text} -> {arg}")

def on_submit():
    print("抽烟：", btn1.isChecked())
    print("喝酒：", btn2.isChecked())
    print("烫头：", btn3.isChecked())
    

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

    btn1 = QCheckBox("抽烟")
    btn2 = QCheckBox("喝酒")
    btn3 = QCheckBox("烫头")
    btn3.setChecked(True)
    
    # btn1.stateChanged.connect(btn_state_update)
    # 给每个CheckBox关联状态变化槽函数
    # arg是stateChanged信号传给函数的参数，代表当前按钮的最新状态：2.选中 0.未选中
    # btn_state_update_func(0, "抽烟", arg) 是将自己的用于区分按钮的参数，和arg混合一起传递给func
    btn1.stateChanged.connect(btn_state_update)
    btn2.stateChanged.connect(lambda arg: btn_state_update_func(1, "喝酒", arg))
    btn3.stateChanged.connect(lambda arg: btn_state_update_func(2, "烫头", arg))

    # 将组件添加到跟布局
    root_layout.addWidget(QLabel("谦哥的三大爱好："))
    root_layout.addWidget(btn1)
    root_layout.addWidget(btn2)
    root_layout.addWidget(btn3)
    
    # 添加提交按钮
    btn_submit = QPushButton("提交")
    btn_submit.clicked.connect(on_submit)
    root_layout.addWidget(btn_submit)

    # 3. 显示窗口
    w.show()
    # 等待app停止
    sys.exit(app.exec_())
