# 闭包

# 嵌套函数，函数内部声明一个函数
def func1():
    print("我是函数1")
    def func2():
        print("我是内部的函数")
    func2()

# func1()

# 私有变量，变量的作用域
# 暂时我们可以把a看成是全局变量
a = 1
def func3():
    print(a)
    b = 2

# func3()
# print(b)

# 一个函数的返回值，也可以是一个函数的引用
def func1():
    print("我是函数1")
    def func2():
        print("我是内部的函数")
        return 1
    return func2

# f1 = func1()
# print(f1)
# print(type(f1))
# f1()

# 闭包
# 如果我们有一个函数，让他可以任意的计算一个值的任意次幂

# def exponent(a,b):
#     return a ** b

def warpper(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of

# 计算一个函数的平方
square = warpper(2)

print(square(2))
print(square(3))
print(square(4))
print(square(5))
"""
在一些语言中，在函数中可以（嵌套）定义另一个函数时，
如果内部的函数引用了外部的函数的变量，则可能产生闭包。

闭包可以用来在一个函数与一组“私有”变量之间创建关联关系。
在给定函数被多次调用的过程中，这些私有变量能够保持其持久性

"""

