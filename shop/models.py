from django.db import models


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
