"""
生成一个1000以内的斐波那契数列
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

然后求列表里所有数字的和

"""

# reduce函数
from functools import reduce
# import functools
# functools.reduce

a = [1,2,3,4,5]
r = 0
for i in a:
    r += i
print(r)

def add(x,y):
    return x + y

result = reduce(add, a,10)
print(result)

print(reduce(lambda x,y:x+y, a))

