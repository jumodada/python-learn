from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.urls import reverse


def hello_world(request):
    return HttpResponse('hello world')

def hello_china(request):
    print(reverse('hello_world'))
    return HttpResponse('hello china')

