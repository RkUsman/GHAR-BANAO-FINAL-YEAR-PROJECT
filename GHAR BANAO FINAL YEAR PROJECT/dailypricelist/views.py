from django.shortcuts import render
from dailypricelist.models import dailypricelst

# Create your views here.
def dailyprice_list(request):
    dpl = dailypricelst.objects.all()  #dpl dail price list object
    return render(request , 'dailypricelist/Dailypricelist.html' , {'dailyprice':dpl})
    
