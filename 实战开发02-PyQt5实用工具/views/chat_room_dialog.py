
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import socket
import threading
import sys
sys.path.append("../")

from common import utils
from ui.Ui_chat_room_dialog import Ui_ChatRoomDialog
from models.chat_models import *
from services.chat_room_manager import ChatRoomManager

class ChatRoomDialog(QDialog):

    def __init__(self, parent=None, room: ChatRoom = None, nickname = "匿名"):
        super().__init__(parent)
        self.ui = Ui_ChatRoomDialog()
        self.ui.setupUi(self)
        # 可以通过此设置，固定对话框的大小
        self.setFixedSize(self.width(), self.height())
        self.room = room
        self.nickname = nickname
        
        self.setWindowTitle(f"聊天室: {room.name} ({room.ip}:{room.port}) [{nickname}]")
        
        self.chat_room = ChatRoomManager(room.ip, room.port, nickname)
        # 将信号on_msg_update_signal关联到槽函数on_msg_update
        self.chat_room.on_msg_update_signal.connect(self.on_msg_update)
        
        self.model = QStringListModel()
        self.ui.lv_members.setModel(self.model)
        self.model.setStringList([
            "智能小车1号(192.168.89.123)", 
            "智能小车2号(192.168.89.123)", 
            "智能小车3号(192.168.89.123)", 
        ])
        
        self.init_ui()
        self.init_data()

    @pyqtSlot(int, object)
    def on_msg_update(self, code, data):
        """用于更新ui界面的 槽函数
        :param code: 数据分类code
        :param data: 数据内容
        """
        print("-------------on_msg_update-----------", threading.current_thread())
        # print("code: ", code, "data: ", data)
        if code == 4: # 群公告
            self.ui.edit_notify.setPlainText(data)
        elif code == 0: # 历史消息
            # 清除已有所有消息
            self.ui.edit_recv.clear()
            for item in data:
                self.append_msg_to_widget(item)
        elif code == 1: # 新消息
            for item in data:
                self.append_msg_to_widget(item)

    def append_msg_to_widget(self, item):
        nickname = item["nickname"]
        from_data = item["from"]
        message = item["message"]
        time = item["time"]
                
        self.ui.edit_recv.appendHtml(
                    f'<font color="blue">{nickname}</font> '
                    f'<font color="gray">({from_data})</font> '
                    f'<font color="red">{time}</font>'
                )
        self.ui.edit_recv.appendHtml(
                    f'<font color="black">{message}</font>'
                )
        self.ui.edit_recv.appendPlainText("")
            

    def init_data(self):
        print("连接服务器：", self.room.ip, self.room.port)
        self.chat_room.enter()
        
    def send_msg(self):
        msg = self.ui.edit_send.toPlainText()
        if msg == "":
            print("消息不能为空")
            return
        
        self.chat_room.send_msg(msg)
        
    def init_ui(self):
        self.ui.btn_send.clicked.connect(self.send_msg)
        self.ui.btn_close.clicked.connect(self.close)
        # nickname = "智能小车"
        # ip, port = "192.168.89.123", 12345
      
        # self.ui.edit_recv.appendHtml(
        #     f'<font color="blue">{nickname}</font>'
        #     f'<font color="gray">({ip}:{port})</font>'
        #     f'<font color="red">2023-10-16 16:01:55</font>'
        # )
        # self.ui.edit_recv.appendHtml(
        #     f'<font color="black">消息内容</font>'
        # )
        
        # self.ui.edit_notify.append("群公告消息")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ip = "192.168.89.198"
    room_info = {
        "name": "90后交友群",
        "ip": ip,
        "port": 8001
    }
    chatroom = ChatRoom(room_info, (ip, 15555))
    dialog = ChatRoomDialog(None, chatroom, "小煤球")
    dialog.show()
    sys.exit(app.exec_())