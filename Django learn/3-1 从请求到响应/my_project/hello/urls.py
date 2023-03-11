from django.urls import path

from hello.views import hello_world, hello_china

urlpatterns = [
    path('python/', hello_world, name='hello_world'),
    path('china/', hello_china, name='hello_china'),
]