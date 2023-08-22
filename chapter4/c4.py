# 类中的一些其他的方法的应用

class Person():
    def run(self):
        print("人会跑")
        print(self)

    # 类方法
    @classmethod
    def class_method(cls):
        print("类方法运行")
        print(cls)

    # 静态方法
    # 也就是说静态方法实际上是与这个类没有什么关系的一个方法
    @staticmethod
    def static_method():
        print("静态方法运行了")


    # 比如我们在一个类中有一个私有变量，那么我想要让外部可以操作这个私有变量那么我们应该怎么办？？
    __age=0

    # property装饰器使得一个方法会变成一个变量
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        # 假设我设置这个年龄的时候，只允许值设置成18到120岁
        if value < 18 or value > 120:
            print("您设置的年龄不在范围内")
            # 程序直接退出
            exit(0)
        else:
            self.__age = value

    @age.getter
    def age(self):
        if self.__age == 0:
            print("请初始化年龄的值以后再使用")
            exit(0)
        else:
            return self.__age


person = Person()
person.run()
person.class_method()

# Person.run()
Person.class_method()
# 类方法可以使用类名直接调用，一般的方法必须使用实例化对象进行调用

person.static_method()
Person.static_method()

# print(person.age())
# print(person.age)

# person.age(1)

person.age = 18
print(person.age)