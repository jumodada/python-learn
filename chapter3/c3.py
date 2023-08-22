# map函数
# 比如我们有一个列表，列表中的元素都是数字，那么请实现，把列表中
# 的所有元素都加1，然后把结果放入到一个新的列表中

my_list = [1,2,3,4,5]
result = []

for i in my_list:
    result.append(i+1)
# print(result)

# map函数的效果展示
def add_one(e):
    return e+2

r = map(add_one, my_list)
print(list(r))

# 加入e传入的是1，那么返回e+3  , 如果e传入的是2 那么返回2-1
def add_two(e):
    if e == 1:
        return e+3
    elif e == 2:
        return e-1
    else:
        return e
r = map(add_two, my_list)
r = list(r)
print(r)


# 结合lamdba表达式
r = map(lambda e:e+1, my_list)
print(list(r))

print(list(map(lambda e:e+1, my_list)))
