from sys import flags
from django.shortcuts import render, redirect 

from laborservices.models import *
from django.http import HttpResponse 
from django.contrib import messages
from laborservices.models import *


# Create your views here.
def carpenterservices(request):
    CarPan = CarPanter.objects.all()  #dpl dail price list object
    return render( request , 'laborservices/Carpenter.html' , {'Carpanter':CarPan})




def booknow_labor(request ,pk):
    trig = 0
    if request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['logusername']
            cus_name = request.POST['yourname']
            address = request.POST['bookaddress']
            mode = request.POST['mode']
            ref = CarPanter.objects.get(pk = pk)

            if(username != request.user.username):
                messages.add_message(request , messages.ERROR , 'Enter correct username')
           
            

            
            else:
            
                bookobj = bookCarpanter(userName =username , Customer_name = cus_name , HomeAddress = address , payment_mode = mode , carpen_name = ref  )
            
                messages.add_message(request , messages.SUCCESS , 'labor order successfully Please call on below mention number')
                bookobj.save()
                
                trig = 1
            
           

        else:
            return render(request , 'laborservices/booknow.html')

    else:
        messages.add_message(request , messages.ERROR , 'You are not login!Please Login First for Booking LABOR')
        

        return render(request , 'core/login.html')
        
    
    return render(request , 'laborservices/booknow.html' , {'flag':trig})
    # return render(request , 'laborservices/booknow.html' )


def show_labor(request):
    user = request.user
    
    show = bookCarpanter.objects.filter(userName = user)
    print(show)


    return render(request , 'laborservices/laborbook.html' , {'show':show})



    





