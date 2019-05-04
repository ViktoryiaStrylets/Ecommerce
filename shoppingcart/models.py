from django.conf import settings
from django.db import models
from shop.models import Item

AuthUser = settings.AUTH_MODEL

class ShoppingcartShoppingcart(models.Model):
    id = models.IntegerField(primary_key=True)
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    itemid = models.ForeignKey(ShopItem, models.DO_NOTHING, db_column='ItemID', blank=True, null=True)  # Field name made lowercase.
    sellerid = models.ForeignKey(ShopSupplier, models.DO_NOTHING, db_column='SellerID', blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='auth_user', blank=True, null=True)
    creation_time = models.DateTimeField()
    updated = models.DateTimeField(blank=True, null=True)
