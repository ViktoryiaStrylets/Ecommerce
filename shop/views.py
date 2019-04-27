from django.shortcuts import render
from django.http import HttpResponse

from .models import Item

def test(request):
    return render(request, 'shop/testview.html')

def search(request):
    items = Item.objects.all()
    return render(request, 'shop/itemview.html', {'items': items})