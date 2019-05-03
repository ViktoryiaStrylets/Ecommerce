from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_home, name='shopping-cart'),
]