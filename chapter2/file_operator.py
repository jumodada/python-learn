# 文件的操作
# 打开一个文件
# f = open("./context.txt",mode="r",encoding="utf-8")
# # 文件内容读取
# result = f.read()
# print(result)
# # 关闭一个文件
# f.close()
"""
r:指的就是文本读取
w:文件写入的意思，如果文件不存在则创建一个文件，注意w权限是先清空文件再进行内容的写入
a:文件追加写入的意思

"""

# 读取文件的代码
# with open("./context.txt",mode="r",encoding="utf-8") as f:
    # 一下子把所有的内容全部都读取出来,读取的结果是一个字符串
    # r = f.read()
    # print(type(r))
    # 只读取一行内容，读取出来的结果是一个字符串
    # r = f.readline()

    # 读取所有的内容，但是readlines会把每一行内容当作一个列表中的元素进行返回
    # 它的返回值是一个列表
    # r=f.readlines()
    # print(type(r))
    # print(r)

# 文件内容写入的代码
# with open("./context1.txt",mode="w",encoding="utf-8") as f:

with open("./context1.txt", mode="a", encoding="utf-8") as f:
    f.write("\n这是我写入的第4行")

