from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test, name='shopping-test'),
    path('', views.search, name='shopping-search'),
]