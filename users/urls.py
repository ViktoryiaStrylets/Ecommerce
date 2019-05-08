from django.urls import path
from . import views
from django.urls import path, include
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('login_page/', views.login_page, name='login_page'),
    path('logout_page/', views.logout_page, name='logout_page'),
]