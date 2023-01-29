from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    mobile_no = models.IntegerField(max_length=10)
    minimum_quantity = models.IntegerField(null=False)
    maximum_quantity = models.IntegerField(null=False)
    pincode = models.IntegerField(max_length=6)

