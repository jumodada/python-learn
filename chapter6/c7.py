d = {
    "a":"a-value",
    "b":"b-value",
    1:11,
    # 2.2:22,
    # True:33
    "c":[1,2,3]
}
print(d)
print(type(d))

# print(d[0])
print(d["a"])
print(d[1])
# 字典的键可以是整数、字符串
# print(d[2.2])
# print(d[True])
print(d["c"])
# 字典的值可以是任意数据类型

# 单独访问字典所有的键
print(d.keys())
# 在对象调用的时候，方法加括号，属性不加括号

# 一次性访问字典所有的值
print(d.values())

