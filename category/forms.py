from django import forms
from . models import *
from django.core.exceptions import ValidationError
class CategoryForm(forms.Form):
    name=forms.CharField( max_length=100, required=True)
    details=forms.CharField(max_length=200,required=True)
    numberproducts=forms.IntegerField(required=True)
    image=forms.ImageField(required=True)
    def clean_name(self):
        userentername=self.cleaned_data['name']
        obj= Category.objects.get(name=userentername).exists()
        if(obj):
            raise ValidationError('name must be unique')
        else:
            return True
            