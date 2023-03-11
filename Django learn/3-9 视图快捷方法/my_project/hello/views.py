from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
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
    """ 请求头练习 """
    # 1. 请求方式
    print(request.method)
    # 2. 请求头信息
    headers = request.META
    print(headers)
    ip = request.META.get('REMOTE_ADDR', None)
    print(ip)
    ua = request.META.get('HTTP_USER_AGENT', None)
    print(ua)
    print('-----------------')
    print(request.headers)
    print(request.headers['User-Agent'])
    print(request.headers['user-agent'])
    # 3. 获取请求参数
    print(request.GET.get('name', '-----'))
    return HttpResponse('响应')


def http_response(request):
    """ Response  """
    resp = HttpResponse('响应内容', status=200)
    print(resp.status_code)
    resp.status_code = 204
    resp['TOKEN'] = 'abc123'
    return resp


def no_data_404(request):
    """ 404 页面 """
    return HttpResponse('404')


def article_detail(request, article_id):
    """
    文章详情，ID是从1000开始的整数
    :param article_id: 文章ID
    """
    if article_id < 1000:
        # return HttpResponseRedirect(reverse('no_data_404'))
        # return redirect('no_data_404')
        # return redirect('/hello/not/found/')
        return redirect('http://www.imooc.com')
    return HttpResponse('文章{}的内容'.format(article_id))