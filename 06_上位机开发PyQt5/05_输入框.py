from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QTextEdit
import sys


def init_widget(w: QWidget):
    # 创建垂直排列的布局Vertical
    layout = QVBoxLayout()
    
    # 单行文本输入-------------------------------------------------------------
    edit = QLineEdit()
    # 设置输入框提示文字
    edit.setPlaceholderText("请输入用户名")
    # 设置默认内容
    edit.setText("abc")
    # 设置输入框最大字符数
    edit.setMaxLength(10)
    layout.addWidget(edit)
    
    # 获取文本框内容
    print("edit: ", edit.text())
    
    edit_pwd = QLineEdit()
    edit_pwd.setPlaceholderText("请输入密码")
    # 设置内容显示模式
    edit_pwd.setEchoMode(QLineEdit.Password) #PasswordEchoOnEdit， Password
    layout.addWidget(edit_pwd)
    
    # 多行文本输入-------------------------------------------------------------
    text_edit = QTextEdit()
    text_edit.setPlaceholderText("请输入个人介绍")
    # 设置文本内容
    text_edit.setPlainText("我叫xxx，来自xxx")
    # text_edit.setHtml("<html><h2>哈哈</h2></html>")
    # 获取已经输入的内容
    print(text_edit.toPlainText())
    layout.addWidget(text_edit)
    
    w.setLayout(layout)

if __name__ == "__main__":
    # 1. 创建应用程序
    app = QApplication(sys.argv)

    # 2. 创建窗口
    w = QWidget()
    # 设置标题
    w.setWindowTitle("输入框")
    # w.resize(640, 480)

    init_widget(w)

    # 3. 显示窗口
    w.show()

    # 等待app停止
    sys.exit(app.exec_())
