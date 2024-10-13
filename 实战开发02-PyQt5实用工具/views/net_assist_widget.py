from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import socket
import threading

from common import utils
from ui.Ui_net_assist_widget import Ui_NetAssistWidget


class NetAssistWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window: QMainWindow = parent
        self.ui = Ui_NetAssistWidget()
        self.ui.setupUi(self)

        self.tcp_client = None

        self.init_ui()

    def update_connect_status(self):
        """根据连接状态，更新界面内容
        self.tcp_client is None 未连接
        self.tcp_client is not None 已连接
        """
        if self.tcp_client is not None:
            # 修改连接按钮文字和图标
            self.ui.btn_connect.setText("断开连接（已连接）")
            icon = QIcon()
            icon.addPixmap(QPixmap(":/icon/connect"))
            self.ui.btn_connect.setIcon(icon)
        else:
            # 修改连接按钮文字和图标
            self.ui.btn_connect.setText("连接网络")
            icon = QIcon()
            icon.addPixmap(QPixmap(":/icon/disc"))
            self.ui.btn_connect.setIcon(icon)

    def run_tcp_client(self, target_ip, target_port):
        # 创建TCP的socket对象
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            target_addr = (target_ip, int(target_port))
            self.tcp_client.connect(target_addr)
            
            print("2.服务器连接成功")
            bar: QStatusBar = self.main_window.statusBar()
            bar.showMessage(f"连接成功：{target_addr}", 3000)
            # ----------------------------------- 更新连接成功后的ui
            local_ip, local_port = self.tcp_client.getsockname()  # 获取本地分配的ip和端口号
            print("sockkname: ", local_ip, local_port)

            # 更新本地ip和port
            self.ui.cb_local_ip.setCurrentIndex(self.ui.cb_local_ip.findText(local_ip))
            self.ui.edit_local_port.setText(str(local_port))
            # 修改连接按钮文字和图标
            self.update_connect_status()

            # -----------------------------------
            # 循环接收服务器发来的数据
            while True:
                bytes_data = self.tcp_client.recv(2048)
                if bytes_data:
                    str_data = utils.decode_data(bytes_data)
                    print("3. str_data: ", str_data)
                    # 把文字内容显示到edit_recv
                    self.ui.edit_recv.append(str_data)
                else:
                    break

        except Exception as e:
            print(e)
            bar: QStatusBar = self.main_window.statusBar()
            bar.showMessage(f"连接失败：{e}", 3000)
        finally:
            print("4. 连接关闭")
            if self.tcp_client is not None:
                self.tcp_client.close()
                self.tcp_client = None
                self.update_connect_status()

    def handle_client_connect(self):
            if self.tcp_client is not None:
                print("已连接，断开连接")
                self.tcp_client.close()
                self.tcp_client = None
                self.update_connect_status()
                return

            target_ip = self.ui.edit_target_ip.text()
            target_port = self.ui.edit_target_port.text()
            print(f"1.连接服务器：{target_ip}:{target_port}")

            if target_ip == "" or target_port == "":
                print("请先输入ip和端口号")
                return

            thread = threading.Thread(
                target=self.run_tcp_client,
                args=(target_ip, target_port),
                daemon=True,  # 守护线程
            )
            thread.start()

    def handle_new_client(self, client_socket: socket.socket, client_addr):
        try:
            while True:
                bytes_data = client_socket.recv(2048)
                if bytes_data:
                    msg = utils.decode_data(bytes_data)
                    self.ui.edit_recv.append(msg)
                else:
                    break
        except Exception as e:
            print(e)
        finally:
            print(f"客户端【{client_addr}】断开")
            client_socket.close()

    def run_tcp_server(self, server_ip, server_port):
        tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server.bind((server_ip, int(server_port)))
        tcp_server.listen(128)  # 变为被动模式

        try:
            while True:
                client_socket, client_addr = tcp_server.accept()
                print(f"有新的客户端【{client_addr}】加入")
                thread = threading.Thread(
                    target=self.handle_new_client,
                    args=(client_socket, client_addr),
                    daemon=True,
                )
                thread.start()
        except Exception as e:
            print(e)
        finally:
            tcp_server.close()

    def handle_server_run(self):
        print("开启服务器")
        server_ip = self.ui.edit_target_ip.text()
        server_port = self.ui.edit_target_port.text()
        if server_port == "":
            print("请先输入端口号")
            return
        thread = threading.Thread(
            target=self.run_tcp_server, args=(server_ip, server_port), daemon=True
        )
        thread.start()

    def on_connect_clicked(self):
        current_mode = self.ui.cb_mode.currentIndex()
        if current_mode == 0:
            self.handle_client_connect()
        elif current_mode == 1:
            # 开关服务器
            self.handle_server_run()

    def on_send_clicked(self):
        # 判断是否已连接
        if self.tcp_client is None:
            print("请先建立连接")
            return

        # 取出用户输入的内容
        text = self.ui.edit_send.toPlainText()
        print("发送：", text)
        self.tcp_client.send(text.encode("UTF-8"))

    def on_mode_changed(self):
        print("current: ", self.ui.cb_mode.currentIndex())
        index = self.ui.cb_mode.currentIndex()
        if index == 0:
            self.ui.label_ip.setText("服务器IP:")
            self.ui.label_port.setText("服务器端口:")
            self.ui.label_local_port.show()
            self.ui.edit_local_port.show()
        else:
            self.ui.label_ip.setText("本地IP:")
            self.ui.label_port.setText("本地端口:")
            self.ui.label_local_port.hide()
            self.ui.edit_local_port.hide()

    def init_ui(self):
        self.ui.edit_target_ip.setText("127.0.0.1")
        self.ui.edit_target_port.setText("8888")
        local_ips = utils.get_local_ip()
        self.ui.cb_local_ip.addItems(local_ips)

        self.ui.btn_connect.clicked.connect(self.on_connect_clicked)
        self.ui.btn_send.clicked.connect(self.on_send_clicked)
        self.ui.cb_mode.currentIndexChanged.connect(self.on_mode_changed)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NetAssistWidget()
    window.show()
    sys.exit(app.exec_())
