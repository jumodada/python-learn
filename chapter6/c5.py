# 抛出异常
# raise


class AgeError(Exception):
    def __init__(self, msg):
        self.msg = msg

class UseError(Exception):
    def __init__(self, msg):
        self.msg = msg

class Person():
    __age = 0

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,value):
        if value <= 18:
            # print("你的年龄设置错误")
            raise AgeError("你的年龄设置错误")
        else:
            self.__age = value
    
    @age.getter
    def age(self):
        if self.__age == 0:
            raise UseError("请先设置年龄后再使用")
        else:
            return self.__age

# 这是作为用户方来使用我们的系统，只不过现在我们还没有一个页面
try:
    person = Person()
    person.age = 1
    print(person.age)
except AgeError as a:
    print(a)
except UseError as u:
    print(u,"年龄还没有设置")
else:
    print("没有捕捉到错误")
finally:
    # 无论代码是否抛出异常，这个代码块的代码都会被运行
    print("资源清除")


# 其他系统中的异常，我们是否可以在抛出的时候添加自己的说明信息
raise Exception("这是我自己的信息")