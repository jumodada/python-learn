# import p
# print(p.a)
# p.p1.f1()

# 结论，我们使用import导入的时候，如果只写到包的层级，那么包下边的模块不可以被使用
# 在init.py文件中我们可以批量的导入一些包，然后通过包名的方式进行直接调用
# print(p.random.randint(1,10))

# import p.p1 as pp
# pp.f1()

from p import *
print(random.randint(1,10))

# import p.p1 as pp
# pp.f1()
# f1()

from p.p1 import f1
f1()


