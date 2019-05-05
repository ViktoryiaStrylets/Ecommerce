from django.shortcuts import render,redirect
from shop.models import Item
from .models import ShoppingCart



def cart_home(request):
    cart_obj, new_obj = ShoppingCart.objects.new_or_get(request)
    item = cart_obj.item
    items = Item.objects.filter(ItemID=item.ItemID)
    # request.session.set_expiry(1000)
    return render(request, 'shoppingcart/cart.html', {'items': items})


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            item = Item.objects.get(ItemID=product_id)
        except Item.DoesNotExist:
             return  redirect("shop/")
    cart_obj, new_obj = ShoppingCart.objects.new_or_get(request)
    cart_obj.item = item
    cart_obj.save()
    return redirect("cart")