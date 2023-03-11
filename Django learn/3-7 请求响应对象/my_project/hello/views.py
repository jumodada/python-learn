from django.http import HttpResponse, JsonResponse
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


def http_request(request):
    """ 请求练习 """
    # 1. 请求方式
    print(request.method)
    # 2. 请求头的信息
    headers = request.META
    print(headers)
    ua = request.META.get('HTTP_USER_AGENT', None)
    print(ua)
    print(request.headers)
    print(request.headers['User-Agent'])
    print(request.headers['user-agent'])
    # 3.获取请求参数
    name = request.GET.get('name', '')
    print(name)
    return HttpResponse('响应')


def http_response(request):
    """ 响应练习 """
    # resp = HttpResponse('响应内容', status=201)
    # resp.status_code = 204
    # print(resp.status_code)
    # return resp
    user_info = {
        'name': '张三',
        'age': 34
    }
    return JsonResponse(user_info)