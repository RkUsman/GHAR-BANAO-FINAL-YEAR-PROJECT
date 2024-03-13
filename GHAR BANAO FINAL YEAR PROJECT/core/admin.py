from xml.parsers.expat import model
from django.contrib import admin
from core.models import *

# for show complet column on admin side

class customerAdmin(admin.ModelAdmin):
    list_display =  ('cus_name' , 'contact' , 'address1' , 'address2' )
class contactAdmin(admin.ModelAdmin):
    list_display =  ('nameofcus' , 'contact' , 'msg' , 'email' )


# Register your models here.
admin.site.register(customer , customerAdmin)
admin.site.register(contactus ,contactAdmin)