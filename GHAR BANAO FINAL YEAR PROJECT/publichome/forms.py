
from django import forms 
from .models import public_readyhouseimggallery
  
class UploadImageForm(forms.ModelForm): 
  
    class Meta: 
        model = public_readyhouseimggallery
        fields = ['image', 'desc' ,'fk'] 