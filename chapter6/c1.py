def division():
    print("===孔融开始分梨啦===")
    # ValueError: invalid literal for int() with base 10: '4.5'
    pear_count = input("现在拥有梨的数量是>>>>>")
    pear_count = float(pear_count)
    pear_count = int(pear_count)
    children = int(input("一共来了几位小朋友>>>>"))
    if children <=0:
        print("小朋友的数量不能小于等于0")
        exit(0)
    result = pear_count/children
    print("每个小朋友分得{}个梨".format(result))

division()
# ZeroDivisionError: division by zero