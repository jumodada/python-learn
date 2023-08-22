"""
BMI公式是: BMI=体重/(身高*身高)

1、当测量者的BMI指数小于18.5时，认为他的体重过轻
2、当测量者的BMI指数大于等于18.5，且小于24时，认为他的体重正常
3、当测量者的BMI指数大于等于24，且小于等于28时，认为他的体重过重
4、当测量者的BMI指数大于28时，认为他的体重属于肥胖行列

"""
# 让用户输入身高,身高单位必须为米
height = input("请输入您的身高,请注意单位是米>")
height = float(height)
# 让用户输入体重，体重单位必须为千克
weight = input("请输入您的体重，请注意单位是千克>")
weight = float(weight)
# 计算出用户输入后的bmi指数
# BMI公式是: BMI=体重/(身高*身高)
bmi = weight/(height*height)

# if height>3 or height<0.5:
#   print("您输入的数据异常，程序结束")
if height<3 and height>0.5:
    #判断 1、当测量者的BMI指数小于18.5时，认为他的体重过轻
    if bmi<18.5:
        print("您的bmi指数是"+str(bmi)+",您的体重太轻了，请注意增重")
    # 2、当测量者的BMI指数大于等于18.5，且小于24时，认为他的体重正常
    elif bmi>=18.5 and bmi<24:
        print("您的bmi指数是"+str(bmi)+",您的身高体重比太标准了")
    # 3、当测量者的BMI指数大于等于24，且小于等于28时，认为他的体重过重
    elif bmi>=24 and bmi<=28:
        print("您的bmi指数是"+str(bmi)+",您已经超重了，请注意减肥")
    # 4、当测量者的BMI指数大于28时，认为他的体重属于肥胖行列
    elif bmi > 28:
        print("您的bmi指数是"+str(bmi)+",您已经属于严重肥胖行列了，请务必进行减肥运行")