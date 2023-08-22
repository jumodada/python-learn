# 循环的跳出
i = 1
while True:
    i = i + 1
    print("循环正在进行"+str(i))

    # continue 继续。 结束本次循环，进行下一次循环
    if i / 2 == 2:
        print("这个时候i的值是4了，结束本次循环，进行下一次循环")
        continue

    if i == 10:
        # break是跳出循环的关键字
        print("这个时候的i的值已经到了10")
        break
