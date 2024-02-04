from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from .models import *




def category_view(request):
    # Fetch product data from your desired source and organize it as a list
    context={'categories':Category.objects.all()}
    return render(request, 'category.html',context)

def categorydetails(request,id):
      obj1= Category.objects.get(id=id)
      context={'category':obj1}
      return render(request,'detailss.html',context)

def addcategory(request):
    if (request.method=='POST'):
        Category.objects.create(name=request.POST['tname'],
                                
                                details=request.POST['tdetails'],
                                numberproducts=request.POST['tnum'],)
        r=reverse("category")
        return HttpResponseRedirect(r)
    return render(request,'add.html')
def categorydelete(request,id):
       Category.objects.filter(id=id).delete()
     
       r=reverse("category")
       return HttpResponseRedirect(r)