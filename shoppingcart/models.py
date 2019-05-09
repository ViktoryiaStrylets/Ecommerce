from django.conf import settings
from django.db import models
from shop.models import Item
from shop.models import Supplier
from django.db.models.signals import pre_save, post_save, m2m_changed

AuthUser = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.auth_user is None:
                cart_obj.auth_user = request.user
                cart_obj.costomerid = request.user
                cart_obj.save()
        else:
            cart_obj = ShoppingCart.objects.new(auth_user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, auth_user=None):
        auth_user_obj = None
        if auth_user is not None:
            if auth_user.is_authenticated:
                auth_user_obj = auth_user
                self.costomerid = auth_user
        return self.model.objects.create(auth_user=auth_user_obj)


class ShoppingCart(models.Model):
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)
    item = models.ManyToManyField(Item, db_column='Item', blank=True)
    total = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, db_column='Total', blank=True, null=True)
    subtotal = models.IntegerField(db_column='subtotal', blank=True, null=True)
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='auth_user', blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    objects = CartManager()
    def __str__(self):
        return 'ShoppingCart'


# def m2m_cart_receiver(sender, instance, action ,*args, **kwargs):
#
#     if 'action' == 'post_add' or 'action' == 'post_remove':
#         items = instance.item.all()
#         total = 0
#         for item in items:
#             total += item.Price
#
#     instance.total = total
#     instance.save()
#
#     m2m_changed.connect(m2m_cart_receiver, sender=ShoppingCart.item.through)


# def pre_save_cart_receiver(sender, instance,*args, **kwargs):
#     instance.total=instance.subtotal
#
#     pre_save.connect(pre_save_cart_receiver, sender=ShoppingCart)