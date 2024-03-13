from django.contrib import admin
from products.models import *

# for show complet column on admin side

class GS_productAdmin(admin.ModelAdmin):
    list_display =  ('id','title' , 'selling_price' , 'discounted_price' , 'description' , 'Category' , 'prod_img' )
class cartAdmin(admin.ModelAdmin):
    list_display =  ('id' , 'user' , 'gs_product' , 'quantity' )

class orderplacedAdmin(admin.ModelAdmin):
    list_display =  ('id' , 'user' , 'Customer' , 'quantity' , 'gs_product', 'order_date' , 'status' )


# Register your models here.
admin.site.register(GS_product , GS_productAdmin)
admin.site.register(cart ,cartAdmin)
admin.site.register(orderplaces ,orderplacedAdmin)


