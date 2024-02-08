from rest_framework import serializers
from product.models import *
from rest_framework.validators import UniqueValidator
class Productserlizer(serializers.Serializer):
     id=serializers.IntegerField(read_only=True,validators=[UniqueValidator(queryset=Product.objects.all())])
     name=serializers.CharField(validators=[UniqueValidator(queryset=Product.objects.all())])

     image=serializers.ImageField(allow_empty_file=True)
     details=serializers.CharField()
     createat=serializers.DateTimeField(read_only=True)
     updateat=serializers.DateTimeField(read_only=True)
     def create(self,validated_data):
         pr=Product()
         pr.name=validated_data['name']
         pr.details=validated_data['image']
         pr.image=validated_data['image']
         pr.save()
         return pr
     def update(self,instance,validated_data):
          instance.name=validated_data.get('name')
          instance.details=validated_data.get('details')
          instance.image=validated_data.get('image')
          instance.save()
          return instance
          
          
       
        
     
     
     