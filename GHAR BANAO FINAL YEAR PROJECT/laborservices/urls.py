from django.urls import path
from laborservices import views
import laborservices
urlpatterns = [
    path('carpenter/' ,views.carpenterservices , name= 'laborservices'),
    path('lbrbooknow/<int:pk>' ,views.booknow_labor , name= 'lbrbooknow'),
    path('showlbrbook/' ,views.show_labor , name= 'showlbrbook'),
]
