# 继承

# object类是所有类的祖宗，无论你是否有明确的指定是否继承它，都会默认的继承object
class Father(object):
    
    a = "爸爸的属性"

    def __init__(self):
        print("父类的构造函数运行了")

    def father_money(self):
        print("爸爸的很多钱")

    def run(self):
        print("爸爸跑步很厉害")

class Mother():
    m = "妈妈的属性"
    a = "妈妈的属性2"
    def face(self):
        print("非常漂亮")
    
    def mother_money(self):
        print("妈妈的很多钱")
    
    def run(self):
        print("妈妈跑步很厉害")
    

# 单继承

# 多继承就是用都好分割，然后写要继承的类名称
# class Son(Father, Mother):
class Son(Mother,Father):
    def __init__(self):

        # vscode默认带出来的代码中super代表的就是父类
        # super().__init__()
        print("子类的构造函数运行了")

# 在子类没有明确声明自己的构造函数的时候，那么默认会调用父类的构造函数

# father = Father()
# print(father)
son = Son()
son.face()
son.father_money()
son.mother_money()

son.run()
print(son.a)
print(son.m)