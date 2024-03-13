from django.db import models

# Create your models here.
class dailypricelst(models.Model):
    proserialnum = models.IntegerField(primary_key=True)  #daily price product_serialnumber
    probrand = models.CharField(max_length=50)
    prodate = models.DateField()
    prounit = models.CharField(max_length=30)
    proprice = models.DecimalField(max_digits=10, decimal_places=2)



