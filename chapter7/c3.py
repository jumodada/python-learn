# 函数的参数类型
def calc_bmi(weight,height):
    if type(weight)!=int:
        return "函数的数据类型不正确，我们只接受数字类型参数"
    bmi = weight/(height*height)
    return bmi
bmi_value = calc_bmi(80,1.8)
print(bmi_value)

# 默认参数

def calc(a=1):
    print(a)
calc()
calc(2)

def calc1(b,a=1):
    print(a,b)
calc1(4)
# 关键字参数
def calc2(b,a=1):
    print(a,b)

calc2(b=1,a=6)
calc2(a=6,b=5)

# 不定长参数
def func1(*param):
    print(param)
    print(type(param))
    for i in param:
        print(i)

func1(1,2,3)
func1(1,2,3,5,6)
# 可变参数
def func2(**param):
    print(param)
    print(type(param))
    for k,v in param.items():
        print(k,v)

func2(a=1,b=2,c=3)




