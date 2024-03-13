from multiprocessing import context
from django.shortcuts import render, redirect 
from gb_readymadehouse.models import *

from django.http import HttpResponse 




# Create your views here.
def gbreadymadehouse(request):
    if 'q' in request.GET:
        q = request.GET['q']
        
        home = houseownerdetail.objects.filter(description__icontains = q)
    else:
        home = houseownerdetail.objects.all()  #dpl dail price list object

    return render( request , 'gb_readymadehouse/readymadehome.html' , {'homes': home})

def gbreadymadehouse_imggallery(request , pk):
    
    galery = readyhouseimggallery.objects.filter(owner = pk)
    

      
    return render( request , 'gb_readymadehouse/readymadehomegallery.html' ,{'imggalery':galery}  )
    
