from xml.parsers.expat import model
from django.contrib import admin
from publichome.models import *

# for show complet column on admin side

class public_houseownerdetailAdmin(admin.ModelAdmin):
    list_display =  ( 'user_name' , 'owner_name' , 'phoneNumber' , 'image' , 'house_price' , 'description' , 'date_time' )


class public_readyhouseimggalleryAdmin(admin.ModelAdmin):
    list_display =  ( 'desc' , 'image' , 'fk'  )


# Register your models here.
admin.site.register(public_houseownerdetail,   public_houseownerdetailAdmin)
admin.site.register(public_readyhouseimggallery,  public_readyhouseimggalleryAdmin)


