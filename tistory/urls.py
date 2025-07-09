from django.urls import path

from tistory import views


urlpatterns = [
    path('', views.index, name='index'),
]