from django import forms
from . models import *



# from django.core.exceptions import ValidationError
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','details','image']
        
    name=forms.CharField( max_length=100, required=True)
    details=forms.CharField(max_length=200,required=True)
   
    image=forms.ImageField(required=True)
    # category=forms.ChoiceField(choices=Category.getcategory())
    # def clean_name(self):
    #     userentername=self.cleaned_data['name']
    #     obj= Product.objects.get(name=userentername).exists()
    #     if(obj):
    #         raise ValidationError('name must be unique')
    #     else:
    #         return True
            