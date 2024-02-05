from django.db import models
from django.utils.timezone import now
from category.models import *
# Create your models here.
class Product(models.Model):
    name=models.CharField( max_length=100)

    image=models.ImageField(upload_to='product/images/',blank=True,null=True)
    details=models.CharField(max_length=200,null=True)
    createat=models.DateTimeField(default=now(),null=True)
    updateat=models.DateTimeField(default=now(),null=True)
    category=models.ForeignKey(Category,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
      return self.name+''+self.email


    @classmethod
    def products(self):
        return self.objects.all()
    @classmethod
    def product_details(cls,id):
        return cls.objects.get(id=id)
    def getpimageurl(self):
        return f'/media/{self.image}'


