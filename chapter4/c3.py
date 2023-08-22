# 数学运算的进阶
# 运算符 
# % 取余数  相除的余数部分
# ** 幂运算  
# // 取整除 相除的整数部分
i = 5
j = 3
print(i%j)
print(i**3) # 5 * 5 * 5
print(i//j)
i = 2
"""
+=  i=i+1   同等于 i += 1
同理可推出
-=
*=
/=
%=
**=
//=


"""
i+=2
print(i)
i+=2
print(i)
a=5
b=2
a-=2
print(a)
a*=10
print(a)
a/=3
print(a)
a%=3
print(a)
b**=2
print(b)
b//=3
print(b)

# 请取出100以内的奇数
i = 0
while True:
    i+=1
    if i % 2 == 0: # 我运算到这里了，如果判断成功了，那么i就是偶数
        # 跳出本次循环
        continue
    print("现在是奇数:"+str(i))
    if i > 98:
        break




