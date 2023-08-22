# 森林运动会
import random
import threading
# 声明一个变量，存储最终的名次
import time

ranking = []
# 声明一个变量，用来存储比赛的距离
distance = 100

def run_method(run_distance, max_sleep_time):
    for i in range(distance):
        # 获取当前线程
        t = threading.current_thread()
        if i % run_distance == 0 and i != 0:
            sleep_time = random.randint(1, max_sleep_time)
            print("{}的休息时间是{}".format(t.name,sleep_time))
            time.sleep(sleep_time)

        print("{}跑的距离是{}".format(t.name,i))

    ranking.append(t.name)
    print("{}完成了比赛".format(t.name))

# 定义兔子线程类
class RabbitThread(threading.Thread):
    def run(self):
        run_method(5,10)
# 兔子线程类
class TortoiseThread(threading.Thread):
    def run(self):
        run_method(1,2)

class ElephantThread(threading.Thread):
    def run(self):
        run_method(10, 15)

class WolfThread(threading.Thread):
    def run(self):
        run_method(15, 20)

class TigerThread(threading.Thread):
    def run(self):
        run_method(15, 20)

class BearThread(threading.Thread):
    def run(self):
        run_method(3,5)

# 实例化每一个动物的线程对象
rabbit_thread = RabbitThread(name="兔子")
tortoise_thread = TortoiseThread(name="乌龟")
elephant_thread = ElephantThread(name="大象")
wolf_thread = WolfThread(name="狼")
tiger_thread = TigerThread(name="老虎")
bear_thread = BearThread(name="熊")


rabbit_thread.start()
tortoise_thread.start()
elephant_thread.start()
wolf_thread.start()
tiger_thread.start()
bear_thread.start()


rabbit_thread.join()
tortoise_thread.join()
elephant_thread.join()
wolf_thread.join()
tiger_thread.join()
bear_thread.join()

print("本次比赛的结果是{}".format(ranking))
