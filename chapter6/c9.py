my_dict = {
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e",
    6:"f"
}

# 如果我用这种方式来进行字典的遍历，那么遍历就是字典的key
for i in my_dict:
    print(i)
for i in my_dict.keys():
    print(i)
    print(my_dict[i])  # 这样我们就实现了一种循环遍历的方式

# 这种方式是直接遍历字典的值
for i in my_dict.values():
    print(i)

# 我们可不可以同时把字典的键和值遍历出来
print(my_dict.items())
# dict_items([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f')])
print(my_dict.items())
print(type(my_dict.items()))
for key,value in my_dict.items():
    print(key)
    print(value)

