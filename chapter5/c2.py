import random
import threading

# 龟兔赛跑的多线程版本

# 距离
import time

distance = 100

# 兔子跑的函数
def rabbit_run():
    for i in range(distance):
        # 兔子每跑5米就让它休息一下
        if i % 5 == 0 and i != 0:
            sleep_time = random.randint(1,10)
            print("兔子的睡觉时间是{}".format(sleep_time))
            time.sleep(sleep_time)

        print("兔子跑的距离是{}".format(i))

    print("兔子完成比赛")

# 乌龟跑的函数
def tortoise_run():
    for i in range(distance):
        print("乌龟跑的距离是{}".format(i))
        time.sleep(1)
    print("乌龟完成比赛")

# 创建线程对象---兔子
rabbit_thread=threading.Thread(target=rabbit_run)

# 创建线程对象--乌龟
tortoise_thread = threading.Thread(target=tortoise_run)

rabbit_thread.start()
tortoise_thread.start()

# join的作用是主线程等待子线程结束后再结束
rabbit_thread.join()
tortoise_thread.join()
