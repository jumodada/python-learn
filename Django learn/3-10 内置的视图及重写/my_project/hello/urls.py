from django.urls import path

from hello.views import hello_china

urlpatterns = [
    path('china/', hello_china, name='hello_china'),
]