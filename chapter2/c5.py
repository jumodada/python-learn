"""
使用装饰器统计兔子函数和乌龟函数的运行时间

兔子每跑5米则随机休息1到10秒
乌龟每跑1米则固定休息1秒

最后统计兔子函数和乌龟函数的运行时间

"""
# 导入一个随机的工具， 这里是导入随机模块
import random
# 导入时间工具
import time

# 定义一个跑道的长度
track_length = 10
# 定义装饰器

def runtime_log(type):
    def runtime(func):
        def inner():
            print("{}开始奔跑了".format(type))
            start_time = time.time()
            func()
            end_time = time.time()
            print("<{}>的运行时间是:{:.2f}".format(type,end_time-start_time))
        return inner
    return runtime


@runtime_log("乌龟")
def wugui():
    for i in range(1,track_length+1):
        print("乌龟跑了{}米".format(i))
        time.sleep(1)

@runtime_log("兔子")
def tuzi():
    for i in range(1,track_length+1):
        if i % 5 == 0:
            time.sleep(random.randint(1,15))
        print("兔子跑了{}米".format(i))

wugui()
tuzi()