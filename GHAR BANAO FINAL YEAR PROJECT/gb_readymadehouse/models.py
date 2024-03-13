from email.mime import image
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class houseownerdetail(models.Model):
     propertyNum = models.IntegerField(primary_key=True)
     owner_name = models.CharField(max_length=50)
     phoneNumber = models.PositiveIntegerField()
     image = models.ImageField(upload_to='readymadehouseimg/')
     house_price = models.CharField(max_length=20)
     description = models.CharField(max_length=200)
     date_time = models.DateField()





class readyhouseimggallery(models.Model):
    owner = models.ForeignKey(houseownerdetail , on_delete=models.CASCADE)
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='readymadehouseimg/')




    