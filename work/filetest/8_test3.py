# coding:utf-8

import glob
import hashlib

#data = {'name': {'path/name': 'content', 'path2/name': 'content'}}
data = {}

def clear(path):
    result = glob.glob(path)

    for _data in result:
        if glob.os.path.isdir(_data):
            _path = glob.os.path.join(_data, '*')
            clear(_path)
        else:
            name = glob.os.path.split(_data)[-1]

            is_byte = False

            if 'zip' in name:
                is_byte = True
                f = open(_data, 'rb')
            else:
                f = open(_data, 'r', encoding='utf-8')
            content = f.read()
            f.close()

            if is_byte:
                hash_content_obj = hashlib.md5(content)
            else:
                hash_content_obj = hashlib.md5(content.encode('utf-8'))
            hash_content = hash_content_obj.hexdigest()

            if name in data:
                sub_data = data[name]

                is_delete = False

                for k, v in sub_data.items():
                    if v == hash_content:
                        glob.os.remove(_data)
                        print('%s will delete' % _data)
                        is_delete = True

                if not is_delete:
                    data[name][_data] = hash_content


            else:
                data[name] = {
                    _data: hash_content
                }

if __name__ == '__main__':
    path = glob.os.path.join(glob.os.getcwd(), '*')
    clear(path)
    for k, v in data.items():
        for _k, v in v.items():
            print(_k, v)
