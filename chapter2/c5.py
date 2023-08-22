import  time
import random
def run(type):
    def start(func):
        def runer():
            start_time = time.time()
            func()
            end_time = time.time()
            print("{} takes {:.2f}".format(type, end_time - start_time))
        return runer
    return start




@run('turtle')
def turtle():
    for i in range(1, 10):
        print("turtle run {} m".format(i))
        time.sleep(1)


turtle()

@run('rabbit')
def rabbit():
    for i in range(1, 10):
        print("rabbit run {} m".format(i))
        if i % 2 == 0:
            time.sleep(random.randint(0, 3))

rabbit()