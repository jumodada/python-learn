# 元组
# 列表  []
# 元组  ()
t = (1,2,3,4,5)
print(t)
print(type(t))
for i in t:
    print(i)
print(t[1])
print(t[-1])
# 列表和元组哪里不一样呢？？
# 我们为元组添加一个元素、
# t.append(6)
# t[1] = 6
# t.remove(2)
# t.pop(1)

"""
总结：列表和元组在声明时的区别是，列表使用[]进行声明，元组使用()进行声明
在访问时没有区别
列表是可以进行增加、删除和修改的操作的，但是元组不支持。
"""

print(t)


