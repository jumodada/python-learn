class Web():

    def index(self):
        print("我是首页")

    def user(self):
        print("我是用户页面")

    def page404(self):
        print("这是统一的404页面")

web = Web()
# 检测
r = hasattr(web,"course")
print(r)

if hasattr(web,"course"):
    pass
else:
    def course():
        print("我是课程页面")
    setattr(web,"course",course)
# web.course()

course1 = getattr(web,"course")
course1()
print(dir(web))
delattr(web,"course")
# web.course()
print(dir(web))


def to_page():
    # url = "www.imooc.com/index"
    # _,page_name = url.split("/")
    # print(page_name)
    page = input("请输入您想去的页面:")
    if hasattr(web,page):
        r = getattr(web,page)
        r()
    else:
        print("用户页面输入错误，进入404页面")
        web.page404()


to_page()