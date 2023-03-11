from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def hello_china(request):
    return HttpResponse('hello china')


def index(request):
    return render(request, 'index.html')


class HomeView(TemplateView):
    template_name = 'home.html'
