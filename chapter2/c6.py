# 孩子的身高=(父亲的身高+母亲的身高)*0.54
father_height = input("请输入父亲的身高:")
father_height = float(father_height)
mother_height = input("请输入母亲的身高:")
mother_height = float(mother_height)
# 运算符的优先级，想要让谁先运算，那么就用括号括起来
child_height = (father_height+mother_height)*0.54
print("孩子的身高是:"+str(child_height))

