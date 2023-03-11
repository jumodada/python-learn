from django.urls import path

from hello.views import hello_world, hello_china, hello_html, hello_year, render_str, render_html, http_request, \
    http_response

urlpatterns = [
    path('python/', hello_world, name='hello_world'),
    path('china/', hello_china, name='hello_china'),
    path('html/', hello_html, name='hello_html'),
    path('year/<int:year>/', hello_year, name='hello_year'),
    path('render/str/', render_str, name='render_str'),
    path('render/html/', render_html, name='render_html'),
    path('http/req/', http_request, name='http_request'),
    path('http/resp/', http_response, name='http_response'),
]