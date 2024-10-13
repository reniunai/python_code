"""
1. 导入模块socket
2. 创建socket套接字
3. 绑定IP&端口（必选）
4. 接收数据
5. 关闭套接字
"""

# 1. 导入模块socket
from socket import *
import utils

# 2. 创建socket套接字
# 参数1：family: AddressFamily
#       IP地址类型：AF_INET IPv4
#       IP地址类型：AF_INET6 IPv6
# 参数2： SocketKind 协议类型
#       SOCK_STREAM: TCP (默认值)
#       SOCK_DGRAM: UDP (默认值)
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 通过此配置避免端口号被占用问题
udp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)

# 3. 绑定IP&端口（可选）  (IP, port)
udp_socket.bind(("", 8888))

print("udp接收器已开启------------------")
# 4. 接收数据recvfrom
# 代码就会阻塞在这里，直到收到数据会自动释放阻塞
# 参数：缓冲区大小，一次最多接收1024个字节的数据
# 返回值：元组 (b'abv123\xb9\xfe\xb9\xfe', ('127.0.0.1', 3333))
#   元素1：数据的字节数组
#   元素2：发送者的(ip,port)元组
bytes_arr, address = udp_socket.recvfrom(1024)

msg = utils.decode_data(bytes_arr)

print("收到来自【{}】消息：{}".format(address, msg))

# 5. 关闭套接字
udp_socket.close()