# 数据类型与数据类型之间的转换

# 我们声明一个数字，是否能转成字符串
a = 1
b = 1.9
print(type(a))
print(type(b))
c="我是大周老师"
print(type(c))
"""
<class 'int'>
<class 'float'>
<class 'str'>
"""
# 整数转换成字符串
print(str(a))
d = str(a)
print(type(d))
print(d)
print(float(a))
# 注意，浮点数转换成整数的时候，只是舍弃了小数点后的数字
print(int(b))
# 注意，是不是字符串不能转换成数字？？？
# print(int(c))
e="11"
print(int(e))
print(type(int(e)))
# 什么样的字符串可以转换成数字？？？
# 必须长的像数字的字符串

# 从键盘中输入  input函数代表着让用户从键盘中输入内容
# result = input()
# print("您输入的内容是:")
# print(result)
# # 字符串的相加操作
# print("您输入的内容是:" + result)

# 字符串与字符串不能够进行减法运算、乘法运算、除法运算
a = "1111"
b = "11"
# print(a/b)

# 问：当我们获取到用户从键盘中输入内容的时候，这个变量是什么数据类型? 字符串
a = input("请输入你的内容:")
print(type(a))

# 问：我们开发计算器时，获取了用户从键盘中输入的内容后，必须要做一下数据类型转换
# 才能够进行算数运算


