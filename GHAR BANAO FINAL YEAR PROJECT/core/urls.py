from django.urls import path
from . import views
import core
urlpatterns = [
    path('login/' ,views.cus_login , name='cus_login') ,
    path('signup/' ,views.sign_up , name='cus_signup') ,
    path('faq/' ,views.faq , name='faq') ,
    path('contactus/' ,views.contact_us, name='contactus') ,
    path('cusprofile/' ,views.cus_profile, name='cusprofile') 
]
