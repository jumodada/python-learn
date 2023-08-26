# coding:utf-8

import glob
import shutil

def update_name(path):
    result = glob.glob(path)

    for index, data in enumerate(result):
        if glob.os.path.isdir(data):
            _path = glob.os.path.join(data, '*')
            update_name(_path)
        else:
            path_list = glob.os.path.split(data)
            # [/home/xxxx, name.txt]
            name = path_list[-1]
            new_name = '%s_%s' % (index, name) # '0_name.txt'
            new_data = glob.os.path.join(path_list[0], new_name)
            shutil.move(data, new_data)

if __name__ == '__main__':
    path = glob.os.path.join(glob.os.getcwd(), '*')
    update_name(path)