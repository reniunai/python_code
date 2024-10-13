"""
1. socket创建一个套接字
2. bind绑定ip和port
3. listen使套接字设置为被动模式
4. accept等待客户端的链接
5. recv/send接收发送数据
"""
import socket
# 1. socket创建一个套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. bind绑定ip和port. (IP可以写空字符串，代表所有网卡都绑定)
tcp_server_socket.bind(("127.0.0.1", 7788))

# 3. listen使套接字设置为被动模式
# 参数表示：等待客户端链接的最大数量。只在windows下生效，其他系统没有限制
# 此时，socket套接字对象由主动连接模式转变为被动接受模式，接受客户端连接
tcp_server_socket.listen(128)

print("服务端已开启，等待客户端接入--------------------------------")

# 4. accept等待客户端的链接(阻塞当前线程，直到有客户端接入)
# 服务器会为连接进来的客户端创建一个socket对象，用于与其收发数据
tcp_client, client_addr = tcp_server_socket.accept()
print("有新的客户端接入：", client_addr)

while True:
    # 5. recv/send接收发送数据 (阻塞)
    client_data = tcp_client.recv(2048)
    if client_data:
        print("收到客户端数据: ", client_data.decode("GBK"))
        # 服务器回复数据
        tcp_client.send("消息已收到!".encode())
        
    else:
        # 收到空字符串，客户端已断开链接
        print(f"客户端 {client_addr} 已断开连接")
        tcp_client.close()
        break

# 关闭服务器tcp套接字，不再接收新的客户端接入，不影响已有客户端交互
tcp_server_socket.close()