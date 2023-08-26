# 清除的是目标文件夹下特定格式的文件

import os
def delete_file(path,file_sub):
    # 列出来path下所有的文件
    files = os.listdir(path)
    # print(files)
    # 在进行具体的文件判断之前我们需要做的是路径拼接
    dir_name = os.path.dirname(__file__)
    target_dir = os.path.join(dir_name,path)
    # print(target_dir)
    for file in files:
        # print(file)
        file_name = file.split(".")[-1]
        print(file_name)
        if os.path.isdir(os.path.join(target_dir,file)):
            print("这是一个文件夹")
            print(file)
            delete_file(os.path.join(path,file),file_sub)
        elif file_name == file_sub:
            # 删除掉这个文件
            print("删除文件")
            os.remove(os.path.join(target_dir,file))
print(os.path.dirname(__file__))
delete_file("clear_file","log")