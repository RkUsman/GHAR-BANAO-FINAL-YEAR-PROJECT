from audioop import add
from ctypes import addressof
import email
from email import message
from http.client import HTTPResponse
from django.shortcuts import HttpResponse
import imp
from logging import logProcesses
from pickle import TRUE
from unicodedata import name
from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import auth
from django.contrib import messages
from core.models import *
from django.contrib.auth.hashers import make_password , check_password
from products.models import *


def home(request):

    Cement = GS_product.objects.all()
    return render(request , 'core/index.html' , {'Cement':Cement})




def cus_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            logusername = request.POST['logusername']
            logpass = request.POST['logpass']
            user = auth.authenticate(username = logusername , password = logpass)
            if user is not None:
                login(request , user)
                return redirect('/')
            else:
                return render(request , 'core/login.html' , {'error': "wrong username or password"})

        else:
            return render(request , 'core/login.html')
    else:
        return redirect('/')





def cus_logout(request):
    logout(request )
    return redirect('/')

cus_name = 0
contact = 0
address1 = 0 
username = 0




def sign_up(request):
    if request.method == "POST":
        try:
            #unique constraint failed i resolve in further process
            user = User.objects.get(username = request.POST.get('logusername')).exists()
           
            messages.warning(request , 'username already exist try differ')
            
            
            return render(request , 'core/signup.html' )
            
            
        except User.DoesNotExist:
            
            
            cus_name = request.POST['cus_name']
            contact = request.POST['contact']
            address1 =request.POST['address1']
            if(not cus_name.isalpha()):
                messages.add_message(request , messages.ERROR , 'customer name not include number or special character and space')
            
            
            elif(not contact.isnumeric()):
                messages.add_message(request , messages.ERROR , 'contact does not include special character')
        
            elif(len(contact) > 11):
                messages.add_message(request , messages.ERROR , 'Enter correct number')
            elif(len(contact) < 11):
                messages.add_message(request , messages.ERROR , 'Enter correct number')
            
            else:
                user = User.objects.create_user(username = request.POST['username'] , password = request.POST['password'])

                customerobj = customer(cus_name  = cus_name , contact = contact , address1 = address1 , user = user )
        
                messages.add_message(request , messages.SUCCESS , 'Account Created successfully')
                customerobj.save()
            
                
            
    return render(request , 'core/signup.html')

 
def cus_profile(request):
    cusprofileobj = customer.objects.all()
    
   
    return render(request , 'core/profilepage.html' , {'profilepage': cusprofileobj})   


def faq(request):
    return render(request , 'core/faq.html')

# def contactus(request):
#     return render(request , 'core/contactus.html')

        
def contact_us(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            nameofcus = request.POST['cusname']
            contact = request.POST['phoneno']
            email = request.POST['email']
            msg = request.POST['msg']

            if(nameofcus != request.user.username):
                messages.add_message(request , messages.ERROR , 'Enter correct username')
            
            
            elif(not contact.isnumeric()):
                messages.add_message(request , messages.ERROR , 'contact does not include special character')
        
            elif(len(contact) > 11):
                messages.add_message(request , messages.ERROR , 'Enter correct number')
            elif(len(contact) < 11):
                messages.add_message(request , messages.ERROR , 'Enter correct number')
            
            else:
            
                contactobj = contactus(nameofcus =nameofcus , contact = contact , email = email , msg = msg )
            
                messages.add_message(request , messages.SUCCESS , 'msg sent successfully')
                contactobj.save()
            
           

        else:
            return render(request , 'core/contactus.html')

    else:
        messages.add_message(request , messages.ERROR , 'You are not login!Please Login First for Contact US')
        return render(request , 'core/login.html')
    
    return render(request , 'core/contactus.html')
        
        
