from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from .models import Item
from .models import Reviews
from .models import Category
from .models import Supplier
from .forms import SearchForm

def sellers(request):
    sellers = Supplier.objects.all()
    return render(request, 'shop/sellerview.html', {'sellers': sellers})

def seller(request, id, name):
    items = Item.objects.filter(SellerID=id)
    return render(request, 'shop/sellerinventoryview.html', {'items': items, 'seller': name})

def shop_all(request):
    items = Item.objects.all()
    request.session['category']=0
    return render(request, 'shop/itemview.html', {'items': items})


def beauty_category(request):
    items = Item.objects.filter(CategoryId=1)
    request.session['category']=1
    return render(request, 'shop/categoryview.html', {'items': items})


def clothing_category(request):
    items = Item.objects.filter(CategoryId=2)
    request.session['category']=2
    return render(request, 'shop/categoryview.html', {'items': items})


def jewelry_category(request):
    items = Item.objects.filter(CategoryId=3)
    request.session['category']=3
    return render(request, 'shop/categoryview.html', {'items': items})


def shoes_category(request):
    items = Item.objects.filter(CategoryId=4)
    request.session['category']=4
    return render(request, 'shop/categoryview.html', {'items': items})


def sort(request):
    if request.POST:
        sort_term = request.POST['sort_options']
        print(sort_term)

        category = request.session['category']
        print(category)

        if sort_term == "low":
            if category==0:
                items = Item.objects.order_by('Price')
                return render(request, 'shop/itemview.html', {'items': items})
            else:
                items = Item.objects.filter(CategoryId=category).order_by('Price')
                return render(request, 'shop/itemview.html', {'items': items})

        if sort_term == "high":
            if category==0:
                items = Item.objects.order_by('-Price')
                return render(request, 'shop/itemview.html', {'items': items})
            else:
                items = Item.objects.filter(CategoryId=category).order_by('-Price')
                return render(request, 'shop/itemview.html', {'items': items})

def search(request):
    if request.POST:
        form = SearchForm(request.POST)

        if form.is_valid():
            search_terms = form.cleaned_data['search_phrase']
            split_search_terms = search_terms.split()

            items = set([])

            for search_term in split_search_terms:
                items = items.union(set(Item.objects.filter(Q(SearchTerm__icontains=search_term) | Q(ProductName__icontains=search_term))))

            return render(request, 'shop/itemview.html', {'items': items})
        else:
            return render(request, 'shop/categoryview.html')


def view_product(request, id, name):
    items = Item.objects.filter(ItemID=id)
    reviews = Reviews.objects.filter(ItemID=id)
    ratings = Reviews.getAvg(reviews, id)
    print(ratings)
    return render(request, 'shop/productview.html', {'items': items})