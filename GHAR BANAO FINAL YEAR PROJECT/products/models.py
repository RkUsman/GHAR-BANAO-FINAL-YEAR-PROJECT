from distutils.command.upload import upload
from email.mime import image
from pickle import TRUE
from pyexpat import model
from sre_constants import CATEGORY
from django.db import models

from core.models import *

# Create your models here.

CATEGORY_CHOICES = (
    ('Cement' , 'cement'),
    ('steel' , 'steel'),
    ('Sand' , 'sand'),
    ('bricks' , 'bricks'),
    ('crush' , 'crush'),
    ('other_const' , 'other_const')
)
class GS_product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    Category = models.CharField( choices= CATEGORY_CHOICES, max_length=30)
    prod_img = models.ImageField(upload_to = 'GSproductimg')

    def __str__(self):
        return str(self.id)
    def __str__(self):
        return str(self.title)


class cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    gs_product = models.ForeignKey(GS_product , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 5)
    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.gs_product.discounted_price

STATUS_CHOICES = (
    ('Acepted' , 'Acepted'),
    ('packed' , 'packed'),
    ('On the way' , 'On the way'),
    ('Deliverd' , 'Deliverd'),
    ('Cancal' , 'Cancal')
)

class orderplaces(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    Customer = models.ForeignKey(customer , on_delete=models.CASCADE)
    gs_product = models.ForeignKey(GS_product , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 5)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50 , choices=STATUS_CHOICES , default='pending')

    @property
    def total_cost(self):
        return self.quantity * self.gs_product.discounted_price

