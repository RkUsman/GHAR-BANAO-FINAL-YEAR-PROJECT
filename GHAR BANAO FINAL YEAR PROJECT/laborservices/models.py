from django.db import models

# Create your models here.
class CarPanter(models.Model):
     lbrNum = models.IntegerField(primary_key=True)
     image = models.ImageField(upload_to='carpenterimages/')
     Name = models.CharField(max_length=30)
     price = models.CharField(max_length=20)
     description = models.CharField(max_length=90)
     def __str__(self):
        return str(self.Name)
     
    

 
class bookCarpanter(models.Model):
     carpen_name = models.ForeignKey(CarPanter , on_delete=models.CASCADE)
     userName = models.CharField(max_length=30)
     Customer_name = models.CharField(max_length=20)
     HomeAddress = models.CharField(max_length=90)
     payment_mode = models.CharField(max_length=40)

   

    

