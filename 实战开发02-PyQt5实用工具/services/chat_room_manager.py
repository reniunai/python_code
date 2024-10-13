import threading
from common import utils
import socket
import json

from PyQt5.QtCore import pyqtSignal, QObject

class ChatRoomManager(QObject):
    
    on_msg_update_signal = pyqtSignal(int, object)
    
    def __init__(self, room_ip, room_port, nickname) -> None:
        super().__init__()
        self.room_ip = room_ip
        self.room_port = room_port
        self.nickname: str = nickname
        self.tcp_client: socket.socket = None
    
    def send_msg(self, msg: str):
        if self.tcp_client is None:
            return
        
        self.tcp_client.send(msg.encode("utf-8"))
    
    def run_forever(self):
        print("---------------------- run_forever --------", threading.current_thread())
          # 连接TCP服务器 room.ip, room.port
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_client.connect((self.room_ip, self.room_port))
        print("连接服务器成功 {}:{}".format(self.room_ip, self.room_port) )
        self.tcp_client.send(self.nickname.encode("utf-8"))
        try:
            while True:
                bytes_data = self.tcp_client.recv(4096)
                if bytes_data:
                    msg = utils.decode_data(bytes_data)
                    print(msg)
                    json_dict = json.loads(msg)
                    code = json_dict["code"]
                    data = json_dict["data"]
                    self.on_msg_update_signal.emit(code, data)
                    # if code == 4:
                    #     print(">> 群公告：", json_dict["data"])
                else:
                    break
        except Exception as e:
            print(e)
        finally:
            self.tcp_client.close()
    
    def enter(self):
        thread = threading.Thread(target=self.run_forever, daemon=True)
        thread.start()
      