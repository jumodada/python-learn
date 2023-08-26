# 函数的递归

# 我们要计算1到5的和，用递归的方式实现
#  在函数内部，自己调用自己

# def digui(i):
#     if i == 5:
#         return
#     print(i)
#     i = i + 1
#     digui(i)
#
# digui(1)


def add(i):
    if i == 1:
        return 1
    print(i)
    return i + add(i-1)
    # retrun 5 + 4 + 3 + 2 + 1
print(add(10))




