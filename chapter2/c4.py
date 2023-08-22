def func3():
    num = yield 1
    print('值为',num)
    num1 = yield num + 10
    print(num1)
    yield  num1 + 10

f3 = func3()
print(f3)
next(f3)
r1 = f3.send(3)
print("r1的值",r1)
# r2 = f3.send(2)
# print("r2的值",r2)
# r3 = f3.send(3)
# print("r3的值",r3)
