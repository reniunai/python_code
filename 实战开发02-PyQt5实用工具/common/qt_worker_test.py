# 使用示例
import sys
import os
import time
import threading

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication
import requests

from qt_worker import Worker


def long_time_recv_task(worker: Worker, title, start):
    counter = start
    thread_name = threading.currentThread().name
    while worker.is_running:
        # 模拟阻塞（等待网络、串口、蓝牙等）
        time.sleep(1)
        # 模拟收到消息
        worker.emit_msg(f"{title} long time task {counter} : {thread_name}")

        counter += 1
        if counter >= 110:
            break

    return "refresh_worker done: {}".format(counter)


@pyqtSlot(object)
def on_result_received(msg):
    thread_name = threading.currentThread().name
    print(f"result: < {msg} > {thread_name}")


def single_recv_thread_test():
    """
    单线程循环接收消息
    :return:
    """
    worker = Worker(long_time_recv_task, args=("消息接收",), kwargs={"start": 100})
    worker.signal_connect(
        msg_handler=lambda msg: print(msg),
        result_handler=on_result_received,
    )
    worker.start()


def pic_download_task(url):
    """
    下载图片, 保存到pic目录
    :param url: 图片地址
    :return:
    """
    response = requests.get(url)
    if response.status_code != 200:
        print("连接图片服务器失败：", response.status_code)
        return
    file_name = url.split('/')[-1]
    # 如果pic目录不存在，则创建
    if not os.path.exists('pic'):
        os.mkdir('pic')

    with open(f"pic/{file_name}", 'wb') as f:
        f.write(response.content)
        # 返回f的绝对路径
        return "{} -> {}".format(url, os.path.abspath(f.name))


def thread_pool_test():
    """
    利用线程池连续下载多个图片文件
    :return:
    """

    pics = [
        "https://www.baidu.com/img/bd_logo1.png",
        "https://c-ssl.duitang.com/uploads/blog/202305/26/EWSwLxqBhV5zZJa.jpg",
        "https://c-ssl.duitang.com/uploads/blog/202305/26/lGSxjBMefx04z33.jpg",
        "https://c-ssl.duitang.com/uploads/blog/202305/26/XxSLogyQCQd9emB.jpg",
        "https://c-ssl.duitang.com/uploads/item/202002/26/20200226215648_yynrr.jpg",
    ]

    for pic in pics:
        worker = Worker(pic_download_task, args=(pic,))
        worker.signal_connect(result_handler=lambda msg: print("保存成功：", msg))
        worker.start_in_thread_pool()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 使用方式1：单线程循环接收消息示例
    single_recv_thread_test()

    # 使用方式2：利用线程池异步执行多个任务示例（下载多个图片文件）
    # thread_pool_test()

    sys.exit(app.exec_())
