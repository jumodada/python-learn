# 自定义异常

class Person():
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        # return self.msg
        return "我是字符串重写的方法"

person = Person("我是人类")
# <__main__.Person object at 0x000002A7576DECD0>
print(person)

# 比如我们有一个系统，对系统中年龄的设置限制到必须18岁以上，如果不是这样我们将抛出以下异常
class AgeError(Exception):
    def __init__(self, msg):
        self.msg = msg


age_error = AgeError("年龄错误")
print(age_error)

print(AgeError("你的年龄输入错误"))

