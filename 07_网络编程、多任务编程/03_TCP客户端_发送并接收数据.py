"""
1. 导入socket模块
2. 创建socket套接字
3. 建立tcp连接（和服务端建立连接）
4. 开始发送数据（到服务端）
5. 等待接受数据
6. 关闭套接字
"""

# 1. 导入socket模块
import socket

# 2. 创建socket套接字
# 参数1：地址类型 family: AddressFamily 地址簇
#       socket.AF_INET: IPv4
#       socket.AF_INET6: IPv6
# 参数2：协议类型
#       SOCK_STREAM TCP
#       SOCK_DGRAM  UDP
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. 建立tcp连接（和服务端建立连接）
addr = ("127.0.0.1", 8080) # 是指服务器(ip, port)元组
tcp_client_socket.connect(addr)

# 4. 开始发送数据（到服务端） 不能直接发字符串，字符串要进行编码
tcp_client_socket.send("你好，中国UTF-8".encode("UTF-8"))

print("------------------------等待接受数据")
# 5. 等待服务器回复消息
# 代码会在这里阻塞，直到服务器回复消息，自动释放阻塞
# 参数__bufsize： 设置缓冲区大小2048字节：一次性最大接收2048个字节。
recv_data = tcp_client_socket.recv(2048)
print("收到数据：", recv_data.decode("GBK"))

# 6. 关闭套接字
tcp_client_socket.close()