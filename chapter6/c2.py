my_list = ["a","b","c","d","e"]
print(my_list)
# 如果我想访问列表中的某一个区间的所有元素
print(my_list[:])
# 从最开始的位置打印到第二个位置
# 但不包含第二个位置
# 大部分情况下都是左闭右开的原则
print(my_list[:2]) 
print(my_list[1:3]) 
# 访问最后一个就从-1开始
print(my_list[-1]) 
print(my_list[-4]) 

# 我们在访问列表的时候[]里边写的都是从左往右数的
print(my_list[-1:-3]) 
print(my_list[-4:-2]) 