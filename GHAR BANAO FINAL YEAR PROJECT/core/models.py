from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):
    cus_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=11)
    address1 = models.CharField(max_length=100) 
    address2= models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.cus_name)


class contactus(models.Model):
    nameofcus = models.CharField(max_length=50)
    contact = models.CharField(max_length=11)
    msg = models.CharField(max_length=500) 
    email = models.EmailField(max_length=254)

    def save(self, *args ,**kwargs):
        super(contactus , self).save(*args ,**kwargs)
    


    



