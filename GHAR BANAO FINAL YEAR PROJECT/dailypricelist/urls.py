from django.urls import path
from . import views
import dailypricelist
urlpatterns = [
    path('dailyprice_lst/' ,views.dailyprice_list , name='dailypricelist') ,
]
