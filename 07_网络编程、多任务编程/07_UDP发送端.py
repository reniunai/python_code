"""
1. 导入模块socket
2. 创建socket套接字
3. 绑定IP&端口（可选）
4. 发送数据
5. 关闭套接字
"""

# 1. 导入模块socket
from socket import *

# 2. 创建socket套接字
# 参数1：family: AddressFamily
#       IP地址类型：AF_INET IPv4
#       IP地址类型：AF_INET6 IPv6
# 参数2： SocketKind 协议类型
#       SOCK_STREAM: TCP (默认值)
#       SOCK_DGRAM: UDP (默认值)
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 3. 绑定IP&端口（可选）  (IP, port)
udp_socket.bind(("", 3333))

# 4. 发送数据
# __data: ReadableBuffer 数据的字节数组
# __address: _Address    目标地址(ip, port)

data = "你好，陌生人2".encode("UTF-8")
addr = ("192.168.89.158", 8888)
udp_socket.sendto(data, addr)

# 5. 关闭套接字
udp_socket.close()