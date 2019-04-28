from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login_page/', views.login_page, name='login_page'),
]