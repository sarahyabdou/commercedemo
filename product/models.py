from django.db import models
from django.utils.timezone import now
# Create your models here.
class Product(models.Model):
    name=models.CharField( max_length=100)

    image=models.CharField(max_length=200,null=True)
    details=models.CharField(max_length=200,null=True)
    createat=models.DateTimeField(default=now(),null=True)
    updateat=models.DateTimeField(default=now(),null=True)
    
def __str__(self):
    return self.name+''+self.email
