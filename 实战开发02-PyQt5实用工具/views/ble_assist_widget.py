from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading
import enum
import sys
sys.path.append("../")

from common import utils
from ui.Ui_bluetooth_assist_widget import Ui_BleAssistWidget
from drivers.driver_bluetooth import BluetoothDataTransfer

class BluetoothState(enum.Enum):
    # 默认状态(未连接)
    DISCONNECTED = 0
    # 扫描中
    SCANNING  = 1
    # 已连接状态
    CONNECTED = 2

class BleAssistWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_BleAssistWidget()
        self.ui.setupUi(self)
        self.current_state = BluetoothState.DISCONNECTED
        self.bdt: BluetoothDataTransfer = None
        
        # 提前声明所有用到的成员属性
        self.devices = []
        
        self.init_ui()
        
        # self.init_data()

    def connect_ble_device(self, device):
        addr, name = device
        self.bdt = BluetoothDataTransfer(addr, name, 1)  # 替换为目标设备的蓝牙地址和端口号
        if not self.bdt.connect():
            print("连接失败")
            return
        
        print("连接成功")
        self.update_ui_state(BluetoothState.CONNECTED)
        
        try:
            while True:
                bytes_arr = self.bdt.receive_data()
                if bytes_arr:
                    msg = utils.decode_data(bytes_arr)
                    # print(msg)
                    self.ui.edit_recv.append(msg)
                else:
                    # 当主动调用disconnect或设备被动断开时
                    # bytes_arr会收到长度为零bytes
                    break
        except Exception as e:
            print(e)
        finally:
            print("蓝牙设备已断开")
            self.bdt = None
            self.update_ui_state(BluetoothState.DISCONNECTED)

    def on_connect_clicked(self):
        if self.current_state == BluetoothState.SCANNING:
            return
        if self.current_state == BluetoothState.CONNECTED:
            self.bdt.disconnect()
            return
        
        # 读取cb_devices中选中的设备
        device_index = self.ui.cb_devices.currentIndex()
        if device_index == -1:
            print("未选择任何设备，请重新选择")
            return
        device = self.devices[device_index]
        print("连接设备:", device)
        t = threading.Thread(target=self.connect_ble_device, 
                             args=(device,), daemon=True)
        t.start()

    def on_send_clicked(self):
        # 取出要发送的消息
        text = self.ui.edit_send.toPlainText()
        if text == "":
            QMessageBox.warning(self, "警告", "请输入要发送的消息")
            return
        if self.bdt == None:
            QMessageBox.warning(self, "警告", "请先连接设备")
            return
        
        print("发送数据：", text)
        # 默认使用utf-8编码字符串
        self.bdt.send_data(text)
        

    def init_ui(self):
        self.ui.btn_connect.clicked.connect(self.on_connect_clicked)
        self.ui.btn_refresh.clicked.connect(self.init_data)
        self.ui.btn_send.clicked.connect(self.on_send_clicked)
        
        # 隐藏已连接设备区域
        self.ui.gb_connected.setHidden(True) # hide()
    
    def get_all_devices(self):
        self.devices = BluetoothDataTransfer.scan_devices()
        print("设备扫描完成，共找到", len(self.devices), "个设备")
        # 启用 扫描按钮
        self.update_ui_state(BluetoothState.DISCONNECTED)
        
        device_names = []
        for device in self.devices:
            name = device[1]
            if name == "":
                name = "Unknown"
            device_names.append(name)
            print(device)
            
        self.ui.cb_devices.addItems(device_names)
    
    def update_ui_state(self, new_state):
        self.current_state = new_state

        if self.current_state == BluetoothState.SCANNING:
            self.ui.btn_refresh.setEnabled(False)
            self.ui.btn_connect.setText("扫描中...")
        elif self.current_state == BluetoothState.CONNECTED:
            self.ui.btn_refresh.setEnabled(True)
            self.ui.btn_connect.setText("断开连接（已连接）")
            self.ui.label_connect_status.setPixmap(QPixmap(":/icon/connect"))
            self.ui.gb_connected.show()
        elif self.current_state == BluetoothState.DISCONNECTED:
            self.ui.btn_refresh.setEnabled(True)
            self.ui.btn_connect.setText("连接设备")
            self.ui.label_connect_status.setPixmap(QPixmap(":/icon/disc"))
            self.ui.gb_connected.hide()
            
        if self.bdt is not None:
            # self.bdt.target_address
            # self.bdt.target_name
            self.ui.label_device_name.setText(f"名称：{self.bdt.target_name}")
            self.ui.label_device_addr.setText(f"地址：{self.bdt.target_address}")
            
    
    def init_data(self):
        print("开始扫描设备！")
        # 禁用扫描按钮
        self.update_ui_state(BluetoothState.SCANNING)
        
        t = threading.Thread(target=self.get_all_devices, daemon=True)
        t.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = BleAssistWidget()
    window.show()

    sys.exit(app.exec_())