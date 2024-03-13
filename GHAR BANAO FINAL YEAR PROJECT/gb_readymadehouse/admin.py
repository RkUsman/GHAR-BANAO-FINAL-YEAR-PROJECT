from xml.parsers.expat import model
from django.contrib import admin
from gb_readymadehouse.models import *

# for show complet column on admin side

class houseownerdetailAdmin(admin.ModelAdmin):
    list_display =  ('propertyNum' , 'owner_name' , 'phoneNumber' , 'image' , 'house_price' , 'description' , 'date_time' )


class readyhouseimggalleryAdmin(admin.ModelAdmin):
    list_display =  ( 'id','owner' ,'desc' , 'image' )


# Register your models here.
admin.site.register(houseownerdetail,   houseownerdetailAdmin)
admin.site.register(readyhouseimggallery,  readyhouseimggalleryAdmin)

