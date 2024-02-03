

# Create your models here.
from django.db import models
from django.utils.timezone import now
# Create your models here.
class Category(models.Model):
    name=models.CharField( max_length=100)
    numberproducts=models.IntegerField(max_length=5,null=True)
    image=models.CharField(max_length=200,null=True)
    details=models.CharField(max_length=200,null=True)
    createat=models.DateTimeField(default=now(),null=True)
    updateat=models.DateTimeField(default=now(),null=True)
    
def __str__(self):
    return self.name+''+self.email
