# 匹配出文本中的数字
import re

"""
在正则表达式中有一些特殊的符号
其中.代表着匹配所有的字符
限定符
* 代表的是重复0次或者是多次 >=0次
+ 代表的是重复1次或者是多次 >=1次
? 代表的是重复0次或者是1次  0，1
{n} 重复n次
{n,} 重复n次或多次   >=n
{n,m} 重复n次到m次    >=n  <=m
"""
"""
元字符
.代表着匹配所有的字符
\w 匹配字母或数字或下划线或汉字
\s 匹配任意的空白符号
\d 匹配数字  0-9
^ shift+6 匹配字符串的开始
$ shift+4 匹配字符串的结尾
# 反义代码
\W 匹配的不是字母或数字或下划线或汉字
\S 匹配的不是任意的空白符号
\D 匹配的不是数字


"""



with open("content.txt", mode="r", encoding="utf-8") as f:
    content = f.read()
    print(content)
    # reg = "."
    # reg = "[012]"
    # reg = "[0-9]"
    # reg = "[0-9]*"
    # reg = "[0-9]+"
    # reg = "[0-9]?"
    # reg = "[0-9]{2}"
    # reg = "[0-9]{2,}"
    # reg = "[0-9]{2,4}"
    # reg = "[a-zA-Z]"

    # 获取到手机号码
    # reg = "1[34567][0-9]{9}"
    # reg = "1[3-7]\d{9}"
    # reg = "^1[3-7]\d{9}"
    # reg = "1[3-7]\d{9}$"

    # 匹配邮箱
    # 当我们使用管道符表示或的关系的时候
    # 正则表达式将会从左往右开始匹配
    # 所以越精准的匹配就要写在左边，
    # 越模糊的匹配就要写在右边
    # reg = "\w+@\w+\.com\.cn|\w+@\w+\.com"
    # reg = "\w+@[163|sina]\.com"
    # reg = "\w+@163\.com|\w+@sina\.com"

    # 验证账号是否合法
    # reg = "[a-z]+qwe[a-z]+"
    # 这种用小括号直接进行括起来的匹配方式叫做捕捉匹配
    # 然后把小括号内部的内容看作是我们要匹配的内容
    # reg = "(\w+@((163)|(sina))\.com)"

    # 不捕捉
    # reg = "\w+@(?:(?:163)|(?:sina))\.com"
    # reg = "\w+@(?:(?:163)|(?:sina))\.com|1[3-7]\d{9}"

    # 匹配网页中的url
    # reg = "http://www\.\w+\.com|https://www\.\w+\.com"
    # reg = "https?://w{3}\.\w+\.com"
    # reg = "(https?://w{3}\.\w+\.com(\.cn)?)"
    reg = "https?://w{3}\.\w+\.com(?:\.cn)?"

    result = re.findall(reg,content)
    print(result)

username = "13923823781"
reg = "\w+@(?:(?:163)|(?:sina))\.com|1[3-7]\d{9}"
result = re.findall(reg,username)
# print(result)
# if result == []:
#     print("您输入的用户名不合法")


"""
零宽断言
(?=reg) 代表的是匹配reg前边的位置
(?<=reg) 代表reg后边的位置
(?!reg) 匹配后边跟的不是reg的位置
(?<!reg) 匹配前边不是reg的位置
"""

