from django.shortcuts import render
from django.http import HttpResponse

from .models import Item


def shop_all(request):
    items = Item.objects.all()
    return render(request, 'shop/itemview.html', {'items': items})


def beauty_category(request):
    items = Item.objects.filter(CategoryId=1)
    return render(request, 'shop/categoryview.html', {'items': items})


def clothing_category(request):
    items = Item.objects.filter(CategoryId=2)
    return render(request, 'shop/categoryview.html', {'items': items})


def jewelry_category(request):
    items = Item.objects.filter(CategoryId=3)
    return render(request, 'shop/categoryview.html', {'items': items})


def shoes_category(request):
    items = Item.objects.filter(CategoryId=4)
    return render(request, 'shop/categoryview.html', {'items': items})