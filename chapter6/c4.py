my_list = ["a","b","c","d","e"]

for i in my_list:
    if i == "b":
        continue
    if i == "d":
        break
    print(i)

# 我们可不可以使用while循环来遍历list呢

# while True:
l = len(my_list)
print(l)
i = 0
while True:
    print(my_list[i])
    i+=1
    if i == l:
        break
print(len("aaaa"))