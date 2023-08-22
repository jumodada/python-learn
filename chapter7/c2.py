# 函数的返回值

def calc(a,b):
    c = a + b
    # print(c)
    return c
    # print(111)

# result = calc(2,3)
# print("我是第九行代码"+str(result))

def calc_bmi(weight,height):
    bmi = weight/(height*height)
    return bmi

bmi_value = calc_bmi(80,1.8)
print(bmi_value)