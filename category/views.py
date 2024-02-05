from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from .models import *
from .forms  import *


def categoryupdate(request,id):
    category=Category.objects.get(id=id)
    context={'category':category}
    
    form=CategoryForm()
    context={'form':form}
    if (request.method=='POST'):
         form= CategoryForm(request,request.POST,request.FILES)
       
         if (form.is_valid):
             obj1=Category.objects.get(id=id)
             obj1.name=request.POST['name']
                                    
             obj1.details=request.POST['details']
             obj1.numberproducts=request.POST['numberproducts']
             obj1.image=request.FILES['image']
           
             obj1.save()
        
             r=reverse("category")
             return HttpResponseRedirect(r)
         else:
            context['msg']='please,fill all fields'
    return render(request,'category/update.html',context)
def category_view(request):
    # Fetch product data from your desired source and organize it as a list
    context={'categories':Category.objects.all()}
    return render(request, 'category.html',context)

def categorydetails(request,id):
      obj1= Category.objects.get(id=id)
      context={'category':obj1}
      return render(request,'detailss.html',context)

# def addcategory(request):
#     if (request.method=='POST'):
#         Category.objects.create(name=request.POST['tname'],
                                
#                                 details=request.POST['tdetails'],
#                                 numberproducts=request.POST['tnum'],
#                                 image=request.FILES['timage'],)
#         r=reverse("category")
#         return HttpResponseRedirect(r)
#     return render(request,'adds.html')
def categorydelete(request,id):
       Category.objects.filter(id=id).delete()
     
       r=reverse("category")
       return HttpResponseRedirect(r)
def addformcategory(request):
      form=CategoryForm()
      context={'form':form}
      if (request.method=='POST'):
            form= CategoryForm(request,request.POST,request.FILES)
        
            if (form.is_valid):
                Category.objects.create(name=request.POST['name'],
                                
                                details=request.POST['details'],
                                numberproducts=request.POST['numberproducts'],
                                 image=request.FILES['image'],
                                )
                r=reverse("category")
                return HttpResponseRedirect(r)
            else:
                context['msg']='Data not compelete'
      return render(request,'addform.html',context)