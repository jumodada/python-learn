print("我是init")

# 这个a是这个模块下的常量，大家伙公用的一个变量
a=10


import random
import time
import sys
# 这个__all__ 变量是用来控制我们在使用*导入的时候，暴漏出去的可导出的函数、变量、模块等
# __all__ = ['time','random']
sys.path.append("e:\imooc_course\python_web\code\part1-2\chapter7\c4")
from p.p1 import *
__all__ = ['time','random','f2']