from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_all, name='shop-all'),
    path('clothing/', views.clothing_category, name='clothing_category'),
    path('beauty/', views.beauty_category, name='beauty_category'),
    path('jewelry/', views.jewelry_category, name='jewelry_category'),
    path('shoes/', views.shoes_category, name='shoes_category'),
    path('search/', views.search, name='shop-search'),
    path('<int:id>/<slug:name>/', views.view_product, name='product-view'),
]