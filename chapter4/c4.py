"""
1、输入了一个数字，然后输入操作符号，然后输入一个数字，然后就算出结果
2、输入了一个数字，然后输入操作符号，然后输入一个数字，然后输入操作符号，然后输入一个数字..
然后就算出结果

"""
# 声明一个变量，来记录到底是第几次运算
number_of_times = 1
while True:
    # 判断到底是不是第一次计算
    if number_of_times == 1:
        result = input("请输入第一个数字:")
        operator = input("请输入操作符号:")
        if operator == "q":
            print("计算程序退出")
            break
        elif operator == "c":
            print("计算器清零，重新开始计算")
            result = 0
            number_of_times = 1
            continue
        second_number = input("请输入第二个数字:")
        result = float(result)
        second_number = float(second_number)
        if operator == "+":
            result += second_number
        elif operator == "-":
            result -= second_number
        elif operator == "*":
            result *= second_number
        elif operator == "/":
            result /= second_number
        else:
            print("没有匹配到正确的操作符，操作符号有错误")

        print("计算的结果是:"+ str(result))
        number_of_times += 1
    else:
        operator = input("请输入操作符号:")
        if operator == "q":
            print("计算程序退出")
            break
        elif operator == "c":
            print("计算器清零，重新开始计算")
            result = 0
            number_of_times = 1
            continue
        second_number = input("请输入第二个数字:")
        result = float(result)
        second_number = float(second_number)
        if operator == "+":
            result += second_number
        elif operator == "-":
            result -= second_number
        elif operator == "*":
            result *= second_number
        elif operator == "/":
            result /= second_number
        else:
            print("没有匹配到正确的操作符，操作符号有错误")

        print("计算的结果是:"+ str(result))
        number_of_times += 1