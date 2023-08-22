# 多态


# 父类
class Animal():
    def action(self):
        print("动物有一些动作")

class Duck(Animal):
    def action(self):
        print("鸭子会游泳")

class Cat(Animal):
    def action(self):
        print("猫咪会上树")

duck = Duck()
cat = Cat()
duck.action()
cat.action()

l = [cat,duck]

for i in l:
    i.action()

def animal_action(a):
    a.action()

animal_action(duck)
animal_action(cat)