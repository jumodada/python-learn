from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse


def hello_world(request):
    return HttpResponse('hello world')

def hello_china(request):
    print(reverse('hello_world'))
    return HttpResponse('hello china')


def hello_html(request):
    """ 响应HTML内容 """
    html = """
    <html>
        <body>
            <h1 style="color:#f00">hello html</h1>
        </body>
    </html>
    """
    return HttpResponse(html)


def hello_year(request, year):
    """ 获取URL指定类型的参数 """
    return HttpResponse('year: {}'.format(year))


def render_str(request):
    """ render_to_string 函数的使用 """
    templ_name = 'hello/index.html'
    html = render_to_string(template_name=templ_name)
    return HttpResponse(html)


def render_html(request):
    """ render 函数的使用 """
    return render(request, 'index2.html')

