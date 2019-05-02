from django.db import models
<<<<<<< HEAD
from django.db.models import Avg
from django.utils.text import slugify
=======
>>>>>>> daa5667323200c78f33750f4ac08192762b38cfc


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
    ReviewID = models.IntegerField(primary_key=True)
    CustomerID = models.IntegerField()
    ItemID = models.IntegerField()
    SellerID = models.IntegerField()
    Ratings = models.IntegerField()
    Review = models.CharField(max_length=255)
    Date = models.DateField(auto_now=True)

    def getAvg(self, id):
        try: 
            return Reviews.objects.filter(ItemID=id).aggregate(Avg('Ratings'))
        except:
            return 0