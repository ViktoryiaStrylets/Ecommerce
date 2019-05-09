from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_home, name='cart'),
    path('update/', views.cart_update, name='cart_update'),
    path('delete/', views.cart_remove, name='cart_remove'),
    path('delete_all/', views.cart_remove_all, name='remove_all')
]