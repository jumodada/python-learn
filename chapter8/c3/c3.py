print("我是主文件入口c3")

# import导入的时候，最后边
# 只能写到模块
import f.f1 as my_f

# f.f1.ff()
my_f.ff()

fc = my_f.FC()
fc.fc_func1()

# 当我们使用from导入的时候
# from后边跟的是一个到模块的路径
# 后边再跟上import关键字
# 在import后边具体写入要导入的
# 类的名称或者是函数的名称
from f.f1 import FC,ff

fc = FC()
fc.fc_func2()
ff()