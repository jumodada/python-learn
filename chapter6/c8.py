my_dict = {
    1:"a",
    2:"b",
    3:"c",
    4:"d"
}

# 如果我们想要向字典中添加元素该怎么操作
dict1 = {
    5:"e"
}
my_dict.update(dict1)
print(my_dict)

# 更新元素,先找到这个元素，然后再对值进行更新
my_dict[1] = "aaaaa"
print(my_dict)

# 我们是否可以根据值更新键

# 当我们字典中存在相同键的时候，前边的值会被覆盖
# 也就是说有一个默认的规则，字典中不可以存在相同的键
# my_dict = {
#     1:"a",
#     2:"b",
#     3:"c",
#     4:"d",
#     1:"dd"
# }

my_dict = {
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"d"
}
print(my_dict)
# 所以结论是，我们不可以根据值来对键进行更新

# 字典的删除操作
my_dict.pop(2)
print(my_dict)

# list  remove
# my_dict.remove("a")
# print(my_dict)
