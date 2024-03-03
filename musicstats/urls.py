from django.urls import path, include
from musicstats import views

urlpatterns = [
    path('', views.hello, name = 'base'),
]