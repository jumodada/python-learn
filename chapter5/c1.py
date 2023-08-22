# 多进程编程代码演示
import time
from multiprocessing import Process
import os

def target_function():
    time.sleep(2)
    print("子进程的ID：{}".format(os.getpid()))

if __name__ == "__main__":
    # print(__name__)
    print("主进程ID:{}".format(os.getpid()))
    ps = []
    for i in range(10):
        p = Process(target=target_function)
        p.start()
        ps.append(p)
    #     让主进程等待子进程运行完成后再停止
    for p in ps:
        p.join()