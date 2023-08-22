class Person():
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b

    def run(self):
        print("run方法运行")

def eat(n):
    print("吃的方法运行{}".format(n))

person = Person(1,2)

print(person.a)

person.__setattr__("eat1",eat)

e = person.__getattribute__("eat1")
e(1)

print(dir(person))


person.eat2 = eat
print(dir(person))
person.eat2(2)