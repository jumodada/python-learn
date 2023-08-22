# 初步学习一下装饰器

# 帮助每一个添加装饰器的函数进行函数名称的打印

def print_function_name(func):
    print(func.__name__)
    # def inner():
    #     pass
    
    # return inner
    return func

@print_function_name
def func1():
    print("函数1运行")


@print_function_name
def func2():
    print("函数2运行")

@print_function_name
def func3():
    print("函数3运行")

# 函数在声明时，如果我们添加了装饰器，那么装饰器在声明时就被调用了

func1()
func2()
func3()