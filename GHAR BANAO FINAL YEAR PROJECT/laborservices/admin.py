
from django.contrib import admin
from laborservices.models import *

# for show complet column on admin side

class CarPantAdmin(admin.ModelAdmin):
    list_display =  ( 'lbrNum', 'image', 'Name' , 'price' , 'description'  )


class bookCarpanterAdmin(admin.ModelAdmin):
    list_display =  ( 'carpen_name', 'userName', 'Customer_name' , 'HomeAddress' , 'payment_mode' )


# Register your models here.
admin.site.register(CarPanter , CarPantAdmin)
admin.site.register(bookCarpanter , bookCarpanterAdmin)