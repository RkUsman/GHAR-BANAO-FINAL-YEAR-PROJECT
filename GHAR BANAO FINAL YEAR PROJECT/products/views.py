import imp
import re
from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.db.models import Q 
# Create your views here.
from django.db import*
from products.models import *
from core.models import *
from django.http import JsonResponse

from products.models import GS_product
class productviewMainpage(View):
    def get(self , request):
        Cement = GS_product.objects.all()
        return render(request , 'core/index.html' , {'Cement':Cement})


class productview(View):
    def get(self , request):
        Cement = GS_product.objects.all()
        return render(request , 'products/products.html' , {'Cement':Cement})


class prod_detView(View):
    def get(self , request , pk):
        Cement = GS_product.objects.get(pk = pk)
        return render(request , 'products/prod_desc.html' , {'Cement':Cement})
# function base view




def addtocart(request):
    user = request.user
    product_id = request.GET.get('Cement_id')
    product = GS_product.objects.get(id = product_id)
    print(product)
    cart(user=user , gs_product = product).save()
    return HttpResponseRedirect('/product/cart')
    
    
    # return redirect('/cart/')


def showcart(request):
    
    
    if request.user.is_authenticated:

        user = request.user
        Cart = cart.objects.filter(user = user)

        amount = 0.0
        shipping_amount = 150.0
        total_amount = 0.0
        cart_product = [p for p in cart.objects.all() if p.user ==user]

        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.gs_product.discounted_price)
                amount += tempamount
                totalamount = amount +shipping_amount

            return render(request , 'products/addtocart.html' , {'CARTS': Cart , 'totalamount': totalamount , 'amount':amount} )
        else:
            return render(request ,'products/emptycart.html' )







def removecart(request):
    
    
    if request.method == 'GET':

        prod_id = request.get['prod_id']
        c = cart.objects.get(Q(GS_product = prod_id) & Q(user = request.user))
        c.delete()

        amount = 0.0
        shipping_amount = 150.0
        total_amount = 0.0
        cart_product = [p for p in cart.objects.all() if p.user ==request.user]

        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.gs_product.discounted_price)
                amount += tempamount
                
            data = {
                'amount':amount,
                
                'totalamount':amount +shipping_amount
            }
            return JsonResponse(data)


# def remove_cart(request, id):
#     if request.user.is_authenticated:

#         if request.method =='POST':
#             finish = cart.objects.get(pk = id)
#             finish.delete()
#             return HttpResponseRedirect('/product/cart')
#     else:
#         return HttpResponseRedirect('/core/login.html')
        

def checkout(request):
    user = request.user
    add = customer.objects.filter(user = user)
    cart_item = cart.objects.filter(user = user)

    amount = 0.0
    shipping_amount = 150.0
    total_amount = 0.0
    cart_product = [p for p in cart.objects.all() if p.user ==request.user]

    if cart_product:
        for p in cart_product:

            tempamount = (p.quantity * p.gs_product.discounted_price)
            amount += tempamount
        totalamount=amount +shipping_amount
    return render(request , 'products/checkout.html' , {'add':add , 'totalamount':totalamount , 'cart_item':cart_item} )

def procedtopay(request):
    user = request.user
    cust = customer.objects.get(user = user)
    
    cart_item = cart.objects.filter(user = user)
    for c in cart_item:
        orderplaces(user = user , Customer = cust , gs_product = c.gs_product , quantity = c.quantity).save()
        c.delete()
    return render(request ,'products/procedtopay.html' )

def disp_customerorder(request):

    op = orderplaces.objects.filter(user = request.user)
    return render(request ,'products/orders.html' , {'orderplace':op} )
    

    
