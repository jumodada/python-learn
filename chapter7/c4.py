# 函数的多个返回值

def calc(a,b):
    a += 1
    b += 1
    return a,b

r = calc(1,2)
print(r)
print(type(r))
r1,r2 = calc(3,4)
print(r1,r2)


def calc1(a,b):
    a += 1
    b += 1
    return (a,b)
r = calc1(1,2)
print(r)
print(type(r))
r1,r2 = calc1(5,6)
print(r1,r2)

# r1,r2,r3 = calc1(5,6)
def calc1(a,b,c):
    a += 1
    b += 1
    c += 1
    return a,b,c

# r1,r2 = calc1(6,7,8)
# 假设我们未来有一个函数有多个返回值，
# 但是我们并不需要所有的返回值，
# 只需要其中一部分
r1,_,_= calc1(1,2,3)
print(r1)
r1,r2,_ = calc1(3,4,5)
print(r1,r2)
_,r1,r2 = calc1(7,8,9)
print(r1,r2)
r1,_,r2 = calc1(7,8,9)
print(r1,r2)