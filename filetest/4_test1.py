# coding:utf-8

import glob

path = glob.os.path.join(glob.os.getcwd(), '*')

# 获取当前路径下所有内容
# 判断每个内容的类型（文件夹还是文件）
# 递归


final_result = []

def search(path, target):
    result = glob.glob(path)

    for data in result:
        if glob.os.path.isdir(data):
            _path = glob.os.path.join(data, '*')
            search(_path, target)
        else:
            if target in data:
                final_result.append(data)
    return final_result


# /home/test1.py   if test1 in /test1/abc.py

if __name__ == '__main__':
    result = search(path, target='test1')
    print(result)
