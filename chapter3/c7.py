student_name = [
"李元修",
"李建国",
"白敬亭", 
"莫怀雨", 
"谢起云", 
"夏亭晚", 
"徐时芳", 
"李清安", 
"李元斐", 
"李拥军"]

r = []
for i in student_name:
    # print(i)
    # if i[0] == "李":
    #     # print(i)

    #     r.append(i)
    if i.startswith("李"):
        print(i)
# print(r)

#  filter
r = filter(lambda x: x.startswith("李"), student_name)
print(r)
# <filter object at 0x000001967C6FBA00>
print(list(r))


