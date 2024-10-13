"""
多任务版TCP服务器

1. 循环等待接受客户端的连接请求
2. 客户端和服务端连接成功
    a. 给每一个客户端初始化一个socket
    b. 给每一个客户端创建一个线程（守护线程）
    b. 每个线程独立处理客户端收发数据
"""
# 初始化TCP服务器socket
import socket
import threading
from utils import decode_data

_BUFFER = 2048

def handle_client(client_socket: socket.socket, client_addr):
    threading_name = threading.current_thread().name
    hello_info = f"欢迎光临【红浪漫】服务器:{threading_name}"
    client_socket.send(hello_info.encode("UTF-8"))
    
    while True:
        # 接收数据
        bytes_data = client_socket.recv(_BUFFER)
        if bytes_data:
            msg = decode_data(bytes_data)
            print(f"收到客户端{client_addr}发来的消息：{msg}")
            client_socket.send("收到！\n".encode())
        else:
            print(f"客户端{client_addr}已断开！")
            client_socket.close()
            break

if __name__ == '__main__':
    # 创建socketTCP服务器
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    port = 8888
    # 绑定IP和端口号
    tcp_server_socket.bind(("", 8888))
    
    # 将socket设置为被动监听，128代表最大的等待数量
    tcp_server_socket.listen(128)
    
    print("服务器已启动：", port)
    
    while True:
        # 不断阻塞，等待接受新的客户端接入
        client_tcp, client_addr = tcp_server_socket.accept()
        # 有新的客户端接进来了
        print(f"新的客户端{client_addr}已连接")
        
        # 此代码不要阻塞
        # handle_client(client_tcp, client_addr)
        thread = threading.Thread(target=handle_client, args=(client_tcp, client_addr))
        thread.daemon = True
        thread.start()
        
            
    tcp_server_socket.close()