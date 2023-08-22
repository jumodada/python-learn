# 日志的打印

def print_log(func):
    print(func)
    return func

@print_log
def func1(a,b):
    print("函数1被运行",a,b)
    
# func1(1,2)

# 函数参数传递演变1

def print_log(func):
    print(func)
    def inner(x,y):
        x += 1
        y += 1
        print(x,y)
        print("参数列表是:",x,y)
    return inner

@print_log
def func1(a,b):
    print("函数1被运行",a,b)
    
# func1(1,2)


# 演变2
def print_log(func):
    print(func)
    def inner(x,y):
        print("参数列表是:",x,y)
        return func(x,y)
    return inner

@print_log
def func1(a,b):
    print("函数1被运行",a,b)
    return a + b
    
# r = func1(10,20)
# print(r)


# 演变3
def print_log(func):
    print(func)
    def inner(*args,**kwargs):
        print("参数列表是:",args,kwargs)
        return func(*args,**kwargs)
    return inner

@print_log
def func1(a,b,c,d,e=1,f=2):
    print("函数1被运行",a,b,c,d)
    return a + b+c+d
    
# r = func1(10,20,30,40,e=1,f=2)
# print(r)


print("演变4的代码")
# 演变4
def print_log(func):
    print(func)
    def inner(*args,**kwargs):
        print("参数列表是:",args,kwargs)
        return func(*args,**kwargs)
    return inner

def print_log(type):
    print(type)
    def warpper(func):
        print(func)
        def inner(*args,**kwargs):
            if type=="控制台":
                print("参数列表是:",args,kwargs)
            elif type == "文件":
                print("我已经把日志输出到文件中了")
            return func(*args,**kwargs)
        return inner 
    return warpper


@print_log("控制台")
def func1(a,b,c,d,e=1,f=2):
    print("函数1被运行",a,b,c,d)
    return a + b+c+d
    
r = func1(10,20,30,40,e=1,f=2)
print(r)


@print_log("文件")
def func2(a,b):
    print("函数1被运行",a,b)
    return a + b
    
r = func2(100,200)
print(r)