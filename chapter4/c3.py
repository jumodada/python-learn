# 私有属性和私有方法的继承问题

# 这就叫函数
def a():
    pass

class Father():
    a = "爸爸的属性"
    __b = "这是爸爸的私有属性"
    
    # 单下划线声明的属性和方法，代表着他们仅在类的内部进行使用，不建议外部调用 
    _c = "这是一个c"

    def __init__(self):
        print("父类的构造函数运行了")

    # 写在类中的函数我们叫做方法
    def father_money(self):
        print("爸爸的很多钱",Father._c)
        print("爸爸的很多钱",self._c)




    # 私有方法的声明,方法名称必须要以双下划线开头，来表示这个方法是私有的
    def __father_knowleger():
        print("爸爸的知识")

    def run(self):
        print("爸爸跑步很厉害",self.__b)
        print("爸爸跑步很厉害",Father.__b)

        # self在类的内部也调用不到私有方法
        # self.__father_knowleger(1)
        # 如果在类的内部调用类的私有方法，需要用类名来直接调用
        Father.__father_knowleger()

class Son(Father):
    pass

father = Father()
# 私有的属性页不能够被实例对象所调用
# print(father.__b)

# 私有方法不能够被实例对象所调用
# father.__father_knowleger()
print(father._c)

son = Son()
# 父类的私有方法不能够被子类继承
# son.__father_knowleger()

# 父类的私有属性不能够被子类继承
# print(son.__b)

# 虽然单下划线的属性被正常的调用和继承了，但是我们并不建议这样使用
print(son._c)

father.father_money()

father.run()


#  Did you mean: '_Father__father_knowleger'?  
#father._Father__father_knowleger()

# 这样写也不建议访问
Father._Father__father_knowleger()