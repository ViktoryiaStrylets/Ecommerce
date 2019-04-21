from django.db import models

class Customer(models.Model):

    Lastname = models.CharField(max_length=255)

    Firstname = models.CharField(max_length=255)

    email = models.EmailField(max_length=255)

    phoneNmuber = models.IntegerField()
