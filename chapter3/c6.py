"""
生成一个1000以内的斐波那契数列
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

然后求列表里所有数字的和

"""
# import functools
# functools.reduce
from functools import reduce

seq = []
# 生成
a = 0
b = 1
while b < 1000:
    seq.append(b)
    # temp = a
    # a = b
    # b = temp + a
    a ,b = b, a+b
    print(seq)

# 两数交换
# temp = a
# a = b
# b = temp + a
# print(a,b)

r = reduce(lambda a,b: a+b, seq)

print(r)