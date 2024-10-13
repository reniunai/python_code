"""
主程序中创建了一个 TaskWorker 实例，将任务添加到任务队列中，并使用定时器定期添加任务。
当任务完成时，TaskWorker 实例会发出信号，主程序中的槽函数会接收到这些信号并进行处理。

 代码具体步骤如下：
 1. 在主程序中定义一个 do_task 函数，该函数用于执行任务。
 2. 在主程序中定义两个槽函数 on_result 和 on_error，分别用于处理任务完成和任务出错的信号。
 3. 创建一个 TaskWorker 实例。
 4. 将 TaskWorker 实例的信号连接到槽函数。
 5. 将任务添加到任务队列中，并使用定时器定期添加任务。
 6. 运行主程序，等待任务执行完成。
"""
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot, QTimer
import sys
import threading
import time

from qt_task import TaskWorker


def do_task(task_arg):
    a, b = task_arg
    rst = a / b
    # Simulate a time-consuming task
    time.sleep(1)  # Pause for 1 seconds
    return f"Task signal_result {a} / {b} = {rst}"


@pyqtSlot(object)
def on_result(result):
    # print(threading.currentThread())
    print("on result: ", result)


@pyqtSlot(Exception)
def on_error(e):
    # print(threading.currentThread())
    print("on error: ", e)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    print("main: ", threading.currentThread())

    task_worker = TaskWorker(do_task)
    task_worker.signal_connect(
        result_handler=on_result,
        finished_handler=lambda: print("on finished"),
        error_handler=on_error,
    )
    task_worker.start()

    # Add tasks to the task manager
    task_worker.join_queue((3, 2))
    task_worker.join_queue((4, 2))
    task_worker.join_queue((5, 2))
    task_worker.join_queue((5, 0))
    print("--------------------------------join")

    # Use a timer to add tasks periodically
    timer = QTimer()
    timer.timeout.connect(lambda: task_worker.join_queue((5, 2)))
    timer.start(3000)  # Add a task every 3 seconds

    # 执行一个10秒后的延时任务
    QTimer.singleShot(10000, lambda: task_worker.stop())

    sys.exit(app.exec_())
