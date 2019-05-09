from django.shortcuts import render,redirect
from shop.models import Item
from .models import ShoppingCart



def cart_home(request):
    cart_obj, new_obj = ShoppingCart.objects.new_or_get(request)
    request.session.set_expiry(1000)
    items = cart_obj.item.all()
    total = 0
    counter = 0
    for item in items:
        total += item.Price
        counter += 1
    cart_obj.total = total
    cart_obj.subtotal = total
    cart_obj.quantity = counter
    cart_obj.save()
    return render(request, 'shoppingcart/cart.html', {"cart": cart_obj})


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            item = Item.objects.get(ItemID=product_id)
        except Item.DoesNotExist:
             return  redirect("shop/")
    cart_obj, new_obj = ShoppingCart.objects.new_or_get(request)
    cart_obj.item.add(item)
    return redirect("cart")


def cart_remove(request):
    print(request.POST)
    product_id = request.POST.get('product_id')
    item = Item.objects.get(ItemID=product_id)
    cart_obj, new_obj = ShoppingCart.objects.new_or_get(request)

    if item in cart_obj.item.all():
       cart_obj.item.remove(item)
    return redirect("cart")

def cart_remove_all(request):
    cart_obj, new_obj = ShoppingCart.objects.new_or_get(request)
    items = cart_obj.item.all()

    for item in items:
        if item in cart_obj.item.all():
            cart_obj.item.remove(item)

    return redirect("cart")