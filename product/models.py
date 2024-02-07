from django.db import models
from django.utils.timezone import now
  # Adjust the import statement according to your project structure


# Create your models here.
class Product(models.Model):
    name=models.CharField( max_length=100,unique=True)

    image=models.ImageField(upload_to='product/images/',blank=True,null=True)
    details=models.CharField(max_length=200,null=True)
    createat=models.DateTimeField(default=now(),null=True)
    updateat=models.DateTimeField(default=now(),null=True)
    # category=models.ForeignKey(Category,null=True,blank=True,on_delete=models.CASCADE)
    # def __str__(self):
    #   return self.name+''+self.email


    @classmethod
    def products(self):
        pass
    
    # def product_details(cls,id):
    #     return cls.objects.get(id=id)
    @classmethod
    def getproductdetails(cls,id):
        return cls.objects.get(id=id)
    def getpimageurl(self):
        return f'/media/{self.image}'
    @classmethod
    def Getall(cls):
        return cls.objects.all()


   
    # @classmethod
    # def Getall(cls):
    #     return cls.objects.all()
   

    # @classmethod
    # def getcategory(self):
    #     return [(t.id,t.name) for t in self.objects.all()]
    # @classmethod
    # def getcategorydetails(cls,id):
    #     return cls.objects.get(id=id)