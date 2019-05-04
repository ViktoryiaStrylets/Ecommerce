from django.shortcuts import render
from.models import ShoppingCart

def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    cart_obj = ShoppingCart.objects.create()
    print(cart_obj.id)
    return render(request, 'shoppingcart/cart.html', {})

