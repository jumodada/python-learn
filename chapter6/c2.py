def division():
    print("===孔融开始分梨啦===")
    # ValueError: invalid literal for int() with base 10: '4.5'
    # 写在try代码块中的代码，是被检测的代码块
    try:
        pear_count = int(input("现在拥有梨的数量是>>>>>"))
        # pear_count = float(pear_count)
        # pear_count = int(pear_count)
        children = int(input("一共来了几位小朋友>>>>"))
        result = pear_count/children
        print("每个小朋友分得{}个梨".format(result))
    # 如果我们直接写except，那么将会捕捉所有的异常
    # except:
    # except Exception:
    # except Exception as e:
    #     print("发生异常了",e)
    except ValueError as v:
        print(v,"你输入的值有错误")
    except ZeroDivisionError as z:
        print(z,"0不可以作为除数")
    
    # UnboundLocalError: cannot access local variable 'children' where it is not associated with a value
    # result = pear_count/children
    # print("每个小朋友分得{}个梨".format(result))

# division()
# ZeroDivisionError: division by zero

# 异常了我们拥有一个异常捕获机制

while True:
    try:
        pear_count = int(input("现在拥有梨的数量是>>>>>"))
        children = int(input("一共来了几位小朋友>>>>"))
        result = pear_count/children
        print("每个小朋友分得{}个梨".format(result))
    except ValueError as v:
        print(v,"你输入的值有错误")
        break
    except ZeroDivisionError as z:
        print(z,"0不可以作为除数")
