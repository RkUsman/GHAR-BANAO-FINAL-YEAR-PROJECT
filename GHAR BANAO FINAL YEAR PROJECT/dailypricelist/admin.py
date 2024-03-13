from xml.parsers.expat import model
from django.contrib import admin
from dailypricelist.models import dailypricelst

# for show complet column on admin side

class dailpricelstAdmin(admin.ModelAdmin):
    list_display =  ('proserialnum' , 'probrand' , 'prodate' , 'prounit' , 'proprice' )


# Register your models here.
admin.site.register(dailypricelst , dailpricelstAdmin)
