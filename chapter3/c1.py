"""
有列表结构如下：goods_info = [
    				("水杯", 12.5, 25),
   				    ("西装", 1280, 3689),
    				("电脑", 7800, 13800),
    				("摄像头", 248.8, 349)
				]
第一列代表商品名称，第二列代表商品折扣价格，第三列代表商品原价

请按照商品折扣数进行从小到大排序
"""
# lambda表达式  匿名函数

# 比如我们想要计算一个圆形的面积
# π*r*r

import math
print(math.pi)
def circle_area(r):
    return math.pi * r * r

res = circle_area(3)
print(res)

result = lambda r:math.pi * r * r

print(result(3))


def calc_function(o):
    if o == "+":
        return lambda a,b: a+b
    elif o == "-":
        return lambda a,b: a-b
    elif o == "*":
        return lambda a,b : a*b


f = calc_function("+")
print(f)
r = f(2,3)
print(r)


l = [-1,2,3,-2]
l.sort()
print(l)
l.sort(reverse=True)
print(l)

l = [(1,-3),(2,-5),(3,1)]
def func(p):
    return p[1]

# 这个key实际上就是一种排序规则，如果传key那么规则就是我们自己进行定义的
l.sort(key=func)
print(l)

l.sort(key=func,reverse=True)
print(l)
