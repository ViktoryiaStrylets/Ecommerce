from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('services/', views.services, name='blog-services'),
    path('customerservice/', views.customerService, name='blog-customerservice'),
]
