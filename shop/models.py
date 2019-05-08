from django.db import models
from django.conf import settings
from django.db.models import Avg
from django.utils.text import slugify

AuthUser = settings.AUTH_USER_MODEL

# Create your models here.
class Item(models.Model):
    ItemID = models.IntegerField(primary_key=True)
    CategoryId = models.IntegerField()
    ProductName = models.CharField(max_length=255)
    BrandName = models.CharField(max_length=255)
    SellerID = models.IntegerField()
    Price = models.DecimalField(max_digits=11, decimal_places=11)
    Size = models.DecimalField(max_digits=11, decimal_places=11)
    Color = models.CharField(max_length=255)
    ProductImage_path = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    SearchTerm = models.CharField(max_length=255)
    Variations = models.CharField(max_length=255)

    def __str__(self):
        return 'Item'

    def slug_name(self):
        return slugify(self.ProductName)

class Reviews(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    ReviewID = models.IntegerField(primary_key=True)
    CustomerID = models.IntegerField(db_column='CustomerID', blank=True, null=True)
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='auth_user', blank=True, null=True)
    ItemID = models.IntegerField()
    SellerID = models.IntegerField()
    Ratings = models.IntegerField(choices = RATING_CHOICES)
    Review = models.CharField(max_length=255)
    Date = models.DateField(auto_now=True)

    def getAvg(self, id):
        try: 
            return Reviews.objects.filter(ItemID=id).aggregate(Avg('Ratings'))
        except:
            return 0

class Category(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    parent_id = models.CharField(max_length=225)

    def __str__(self):
        return 'Category'

class Supplier(models.Model):
    SellerID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    CompanyName = models.CharField(max_length=255)
    AddressID = models.IntegerField()

    def __str__(self):
        return 'Supplier'

