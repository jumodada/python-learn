"""
CRUD
增删改查
create \ read \ update \ delete
"""
# 修改列表中的元素
# 列表元素的增加
my_list = ["a","b","c","d","e"]
print(my_list)
my_list.append("f")
print(my_list)
# 列表元素值的修改,更新
# 你要更新哪一个数据，必须先能访问到这个数据
my_list[2] = "G"
print(my_list)
# 列表元素值的删除
# 1、根据值删除
my_list.remove("d")
print(my_list)
# 2、根据索引来删除
my_list.pop(1)
print(my_list)




