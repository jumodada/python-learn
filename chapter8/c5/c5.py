

# if __name__ == "__main__":
#     print("你好世界")

# __main__ 一般来说代表着一个程序运行的入口  main.py
print(__name__)

from time_utils import my_time
my_time()
from db.db_utils import my_db
my_db()

# 当我们直接运行__name__这个变量所在的文件（模块）的时候，这个__name__的值就是__main__
# 当我们不直接运行__name__这个变量所在的文件（被导入运行的时候），那么这个__name__的值就是所在路径的名称

# 我们一般在主（入口）运行文件当中
# if __name__ == "__main__":
#     print("你好世界")
# 由这段来进行判断这个文件到底是不是主运行文件

# 如果不是主入口文件运行时，我们可以把
if __name__ == "__main__":
    print("你好世界")
# 当成调试的入口