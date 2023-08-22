# 字符串的格式化  
# i = "python web开发"
# i = input("请输入你想要学习的课程名称:")
# s = "我来学习%s课程" % i
# print(s)
"""
%s 这是一个占位符，后边将会用一个参数进行替代 注意这个参数是一个字符串
%d 这是一个整数类型
%f 这是一个浮点数类型
"""
# print("我学习课程已经有%d个小时了" % 10)
# print("我学习课程已经有%f个小时了" % 10.501)

# format格式化
s = "我跟着%s，学习%s课程" % ("大周老师","Python开发")
print(s)
s = "我跟着{}，学习{}课程".format("大周老师111","Python开发1111")
print(s)
r = "{0}跟着{1},学习{2},{0}学习了{3}个小时".format(
    "小明同学","Mr.zhou","Python开发课程",100)
print(r)

r =  """{student_name}跟着{teacher_name},学习{course_name},{student_name}学习了{study_time}个小时
""".format(
    teacher_name="Mr.zhou",student_name="小明同学",course_name="Python开发课程",study_time=100)
print(r)

# 保留小数位的输出
print("请保留小数点后2位{:.2f}".format(3.141592657))
# 保留符号
print("请保留小数点后2位{:+.2f}".format(-3.141592657))
print("请保留小数点后2位{:+.2f}".format(+3.141592657))
print("请保留小数点后2位{:.0f}".format(3.141592657))
print("百分号的形式显示{:.2%}".format(3.141592657))