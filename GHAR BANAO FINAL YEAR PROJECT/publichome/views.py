from multiprocessing import context
from django.shortcuts import render, redirect 
from publichome.models import *
from django.contrib import messages
from django.http import HttpResponse 
from .forms import *




# Create your views here.
def pp_house(request):
    
    if 'q' in request.GET:
        q = request.GET['q']
        
        home = public_houseownerdetail.objects.filter(description__icontains = q)
    else:
        home = public_houseownerdetail.objects.all()  #dpl dail price list object

        return render( request , 'publichome/public_sell_home.html')




def sell_home(request):
    if request.method == "POST":

        
        
    
        user_name = request.POST['user_name']
        owner_name = request.POST['ownername']
        phoneNumber = request.POST['ownercontact']
        image = request.POST['sellpic']
        house_price = request.POST['pricedemand']
        description = request.POST['address']
        date_time = request.POST['date']
        
        print(user_name)
        print(image)
        if(not phoneNumber.isnumeric()):
            messages.add_message(request , messages.ERROR , 'contact does not include special character')
        
        elif(len(phoneNumber) > 11):
            messages.add_message(request , messages.ERROR , 'Enter correct number')
        elif(len(phoneNumber) < 11):
            messages.add_message(request , messages.ERROR , 'Enter correct number')
        
            
        else:
            pbhouseobj = public_houseownerdetail(user_name  = user_name , owner_name = owner_name , phoneNumber = phoneNumber , image = image,
            house_price = house_price , description = description , date_time =date_time )
            messages.add_message(request , messages.SUCCESS , 'HOME ADDED successfully')
            pbhouseobj.save() 
                           
            
    return render(request , 'publichome/sellform.html' )



def pp_imggallery(request , pk):
    
    galery = public_readyhouseimggallery.objects.filter(fk = pk)
    

      
    return render( request , 'publichome/publichomegallery.html' ,{'imggalery':galery}  )

def showpbhomedata(request):
    res = public_houseownerdetail.objects.all()
    
    

    # context = {
    #         'user_name': user_name,
    #         'owner_name':owner_name,
    #         'phoneNumber':phoneNumber,
    #         'image':image,
    #         'house_price':house_price,
    #         'description':description,
    #         'date_time':date_time,
    #     }
        
    return render(request , 'publichome/public_sell_home.html' , {'res':res})




def upload_imggallery(request):
    
    if request.method == 'POST': 
        submitted_form = UploadImageForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            submitted_form.save()
            messages.add_message(request , messages.SUCCESS , 'Pic Upload Successfully you can check in main page a well')
        else:
            messages.add_message(request , messages.ERROR , 'Some ERROR Please the correct filetype')
    
    form = UploadImageForm()
    context = {
    
        'form': form,
        'images': public_readyhouseimggallery.objects.all
    }
    return render(request, 'publichome/public_imggalleryform.html', context=context)
    
    
    

