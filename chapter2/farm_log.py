import random

log_file = open("farm.log",mode="a",encoding="utf-8")
# 记录牛吃草的次数
cow_eat_count = 0
# 记录草被雨水灌溉的次数
grass_drink_count = 0

while True:
    # 明确循环结束的条件
    if cow_eat_count == 5:
        print("牛长大了，程序运行结束了")
        log_file.write("\n牛长大了，程序运行结束了")
        break

    if grass_drink_count == 3:
        cow_eat_count += 1
        print("小牛开始吃草了，现在吃的时第{}次".format(cow_eat_count))
        log_file.write("\n小牛开始吃草了，现在吃的时第{}次".format(cow_eat_count))
        grass_drink_count = 0
        print("重置草灌溉的次数")
        log_file.write("\n重置草灌溉的次数")
    else:
        if random.randint(1,5)==1:
            grass_drink_count += 1
            print("下雨了，小草开始长大了，现在小草{}岁了".format(grass_drink_count))
            log_file.write("\n下雨了，小草开始长大了，现在小草{}岁了".format(grass_drink_count))
        else:
            print("没有下雨，小草没有成长")
            log_file.write("\n没有下雨，小草没有成长")

log_file.close()

