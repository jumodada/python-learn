# 我们是基于关键字搜索做的聊天机器人

rebot = "小可爱"
while True:
    user_meassage=input("我说:")
    if "名字" in user_meassage:
        print("{0}:我叫{0}".format(rebot))
    elif user_meassage.find("学习")>-1:
        print("{0}:我跟着大周老师学习呀".format(rebot))
    elif user_meassage.find("老师")>-1:
        print("{0}:我真鄙视你呀，你连大周老师都不知道！".format(rebot))
    elif "水果" in user_meassage:
        print("{0}:我喜欢吃的水果有很多呀，比如说香蕉苹果大鸭梨呀".format(rebot))
    elif "再见" in user_meassage:
        print("{0}:再见，{0}会永远想你了，欢迎你再来聊天啊".format(rebot))
        break
    else:
        print("{0}:对不起亲爱的朋友，我没有理解你说的是什么".format(rebot))


