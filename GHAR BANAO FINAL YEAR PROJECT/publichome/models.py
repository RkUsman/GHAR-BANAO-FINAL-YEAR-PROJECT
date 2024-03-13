from email.mime import image
from pickle import NONE
from django.db import models


# Create your models here.

class public_houseownerdetail(models.Model):
     id = models.BigAutoField(primary_key=True)
     user_name = models.CharField( max_length=60)
     owner_name = models.CharField(max_length=50)
     phoneNumber = models.PositiveIntegerField()
     image = models.ImageField(upload_to='publicreadymadehouseimg')
     house_price = models.CharField(max_length=20)
     description = models.CharField(max_length=200)
     date_time = models.DateField()
     def __str__(self):
          return str(self.id)
     def __str__(self):
        return str(self.owner_name)



class public_readyhouseimggallery(models.Model):
     fk = models.ForeignKey(public_houseownerdetail , on_delete=models.CASCADE , default=1)
     desc = models.CharField(max_length=200)
     image = models.ImageField(upload_to='publicreadymadehouseimg')




    