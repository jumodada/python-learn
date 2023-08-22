# 声明一个大雁  类

# 这个class就代表了类声明的关键字  WildGoose是类的名称
# 注意：给类的名称其名字的时候，我们需要采用驼峰命名法，就是单词的首字母需要大写
class WildGoose():
    # 类的属性：就是描述这个类的一些特征吧
    # 所以，类的属性通常描述类的那些公共的，更加通用的特征
    neck = "长长的脖子"
    wing = "宽厚的翅膀"
    leg = "健壮的腿"

    # 构造函数, self其实就是实例对象
    def __init__(self,name):
        print("大雁的构造函数运行了")
        self.name = name

    # 大雁都会飞
    def fly(self):
        print("大雁{}飞".format(self.name))


# 如何访问类的属性
print(WildGoose.leg)
# 尽管我们可以通过类的名称显示的调用构造函数，但是这样的调用是错误的，我们一般不这样做
# print(WildGoose.__init__(1))
# 实例化 wg1就是实例化对象
wg1 = WildGoose("小白")
print(wg1.name)
# print(WildGoose.a)
print(wg1.neck)

wg2 = WildGoose("小灰")
print(wg2.name)

wg2.fly()
wg1.fly()
