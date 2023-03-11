# coding:utf-8

from shutil import copytree, rmtree, move

# copytree('test3', 'test4')  # 目标地址不能存在，否则会报错

# rmtree('test4')
# 1 test4 必须要存在，否则会报错
# 2 test4 中 是否有文件 都可以正常删除，只要目标文件夹存在

# move('test3', 'test4')
# 当目标路径不存在，并且和来源目录属于相同路径下，属于重命名

move('test4', 'test2/test3')



