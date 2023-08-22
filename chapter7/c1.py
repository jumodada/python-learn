# __dict__ 属性

class Father(object):
    __name = "爸爸的名字"
    c = "类属性c"

    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
    # 私有方法
    def __knowledge(self):
        print("爸爸的知识体系")


father = Father(111,222)
# father.__knowledge()

print(Father.__dict__)
# 这就是私有方法的访问方式，但是我们并不建议这样访问
# 因为既然写了私有方法了，默认就是不希望我们访问
father._Father__knowledge()

# 当我们在一个类中进行私有方法的声明时，Python默认对我们的私有方法进行了名称上的修改
# 在原有的方法前边加上了_类名

"""
{'__module__': '__main__',
 '_Father__knowledge': <function Father.__knowledge at 0x000002A3844E9C60>,
   '__dict__': <attribute '__dict__' of 'Father' objects>, 
   '__weakref__': <attribute '__weakref__' of 'Father' objects>, 
   '__doc__': None}

"""


# 我们想要获取到一个类中的所有属性和方法，包含魔术方法，我们应该怎么办
print(dir(Father))

"""
['_Father__knowledge', 
'_Father__name', 
'__class__', 
'__delattr__', 
'__dict__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

"""


a = 1
b = 2
print(a + b )

class A():
    def __init__(self,a) -> None:
        self.a = a
    
    def __add__(self, other):
        print("调用了add方法，但是这里我把加法运算改成了减法运算")
        return self.a - other
print(dir(int))

a = A(3)
print(a+1)

print(dir(Father))
print("----------")
print(dir(father))
