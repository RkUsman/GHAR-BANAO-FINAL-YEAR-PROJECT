from django.urls import path
from gb_readymadehouse import views
import gb_readymadehouse
urlpatterns = [
    path('readymadehome/' ,views.gbreadymadehouse, name= 'readymadehome'),
    path('readymadehomegallery/<int:pk>' ,views.gbreadymadehouse_imggallery, name= 'readymadehomegallery'),
]
