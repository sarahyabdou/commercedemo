

# Create your models here.
from django.db import models
from django.utils.timezone import now
# Create your models here.
class Category(models.Model):
    name=models.CharField( max_length=100)
    numberproducts=models.IntegerField(max_length=5,null=True)
    image=models.ImageField(upload_to='category/images/',blank=True,null=True)
    details=models.CharField(max_length=200,null=True)
    createat=models.DateTimeField(default=now(),null=True)
    updateat=models.DateTimeField(default=now(),null=True)
    
    def __str__(self):
      return self.name+''+self.details
    @classmethod
    def categories(self):
        return self.objects.all()
    @classmethod
    def category_details(cls,id):
        return cls.objects.get(id=id)
    def getimageurl(self):
        return f'/media/{self.image}'
    @classmethod
    def getcategory(self):
        return [(t.id,t.name) for t in self.objects.all()]
    
    
    
    
    
    
    

    











