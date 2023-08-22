class Person():
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b

    def run(self):
        print("run方法运行")

person = Person(1,2)

print(person.a)

# c_value = input("请输入你要添加属性的值")

# person.c = c_value 
# print(person.c)

c = input("请输入你要添加的属性名称")
c_value = input("请输入你要添加属性的值")

person.__setattr__(c,c_value)
result = person.__getattribute__(c)
print(result)