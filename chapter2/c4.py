# yield  生成器

def func1():
    return 1
    print(222)

# f = func1()
# print(f)

def func2():
    print("函数func2被调用1")
    yield 2
    print("函数func2被调用2")
    yield 3
    print("函数func2被调用3")
    yield 4

# f2 = func2()
# print(f2)
# # 启动生成器对象
# r2 = f2.__next__()
# print(r2)
# r3 = f2.__next__()
# print(r3)
# r4 = f2.__next__()
# print(r4)

# for i in range(5):
#     print(i)

# for f in f2:
#     print(f)

def func3():
    num = yield 1
    print(num)
    num1 = yield num + 10
    print(num1)
    yield  num1 + 10

f3 = func3()
print(f3)
r1 = f3.send(None)
print("r1的值",r1)
r2 = f3.send(2)
print("r2的值",r2)
r3 = f3.send(3)
print("r3的值",r3)

# 生产者与消费者的案例
def customer():
    while True:
        n = yield
        if not n:
            return
        print("消费者消费了{}号包子".format(n))

# 生产者代码
def product(c):
    # 消费者的生成器启动
    c.send(None)
    for i in range(5):
        print("生产者生产了{}号包子".format(i))
        # 我们需要告诉消费者可以消费了
        c.send(str(i))

c = customer()
product(c)
