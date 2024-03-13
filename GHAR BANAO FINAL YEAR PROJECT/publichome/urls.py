from django.urls import path
from publichome import views

urlpatterns = [
    path('sellhome/' ,views.sell_home, name= 'sellhome'),
    path('pbshowdata/' ,views.showpbhomedata, name= 'pbshowdata'),
    
    path('uploadimggallery/' ,views.upload_imggallery, name= 'uploadimggallery'),
    path('ppreadymadehomegallery/<int:pk>' ,views.pp_imggallery, name= 'ppreadymadehomegallery'),
]
