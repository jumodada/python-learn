# coding:utf-8

import glob

path = glob.os.path.join(glob.os.getcwd(), '*')

# 获取当前路径下所有内容
# 判断每个内容的类型（文件夹还是文件）
# 递归

final_result = []

def search(path, target):
    result =  glob.glob(path)

    for data in result:
        if glob.os.path.isdir(data):
            _path = glob.os.path.join(data, '*')
            print('path is %s' % _path)
            search(_path, target)
        else:
            f = open(data, 'r')
            try:
                content = f.read()
                if target in content:
                    final_result.append(data)
            except:
                print('data read failed: %s' % data)
                continue
            finally:
                f.close()

    return final_result


if __name__ == '__main__':
    result = search(path, target='dewei')
    print(result)
