from django.urls import path
from django.views.generic import TemplateView

from hello.views import hello_china, index, HomeView

urlpatterns = [
    path('china/', hello_china, name='hello_china'),
    path('index/', index, name='index'),
    path('home/', HomeView.as_view(), name='home'),
]