
def print_log(type):
    print(type)
    def warpper(func):
        print(func)
        # 接受位置参数和关键字参数
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
    
r = func1(1,2,3,4, e=1)
print(r)


@print_log("文件")
def func2(a,b):
    print("函数1被运行",a,b)
    return a + b

r = func2(100,200)
print(r)