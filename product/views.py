from django.shortcuts import render,reverse

from django.http import HttpResponseRedirect
from .models import *

# Create your views here.
# def home(request):
#     return HttpResponse("iti cairo university")



def product_view(request):
    # Fetch product data from your desired source and organize it as a list
    context={'products':Product.objects.all()}
    return render(request, 'product.html',context)

def productdetails(request,id):
      obj1= Product.objects.get(id=id)
      context={'product':obj1}
      return render(request,'product/details.html',context)
  


def addproduct(request):
    if (request.method=='POST'):
        Product.objects.create(name=request.POST['tname'],
                                
                                details=request.POST['tdetails'],)
        r=reverse("product")
        return HttpResponseRedirect(r)
    return render(request,'add.html')
def productdelete(request,id):
       Product.objects.filter(id=id).delete()
     
       r=reverse("product")
       return HttpResponseRedirect(r)