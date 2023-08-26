import os

print(__file__)
# 我们如何获得当前文件所在的文件夹
dir_path = os.path.dirname(__file__)
print(dir_path)

# 我如果想要获取当前文件夹下所有的文件(文件的说法是既包含我们平时理解的单个文件，也包含文件夹)
# dir_list = os.listdir(dir_path)
dir_list = os.listdir("E:\imooc_course\python_web\code\part1_3\chapter2")
print(dir_list)
# 判断某一个文件是不是文件夹
print(os.path.isdir(__file__))
print(os.path.isfile(__file__))
# 创建一个新的文件夹
# os.mkdir("aa/bb/cc")
# 这个创建失败了，说明如果我们想要使用mkdir创建文件夹时，那么里边的路径表示的内容必须存在
# os.mkdir("dd/ee/ff")
# 会使用搜索引擎
# os.makedirs("dd/ee/ff")

# 删除一个文件夹
# os.rmdir("dd/ee/ff")
# rmdir只能删除一个空文件夹
# os.rmdir("dd/ee")
# removedirs 它也不能删除一个非空目录
# removedirs 一层一层的去删除空文件夹
# os.removedirs("aa/bb/cc")


# 重命名
# os.rename("dd/ee","dir1")  # 这不是剪切么
# os.rename("dir1","dd/dir2")

# 路径拼接
print(os.path.join("aa/bb","dd.txt"))



