from django.shortcuts import render,reverse

from django.http import HttpResponseRedirect
from .models import *

from .forms  import *
# Create your views here.
# def home(request):
#     return HttpResponse("iti cairo university")

# def productupdate(request,id):
#     product=Product.product_details(id)
#     context={'product':product}
#     if (request.method=='POST'):
#         if(request.POST['tname'] !='' and  request.POST['tdetails'] !=''):
        
#             Product.objects.filter(id=id).update(name=request.POST['tname'],
                                    
#                                     details=request.POST['tdetails'],)
#             r=reverse("product")
#             return HttpResponseRedirect(r)
#         else:
#             context['msg']='please,fill all fields'
#     return render(request,'product/update.html',context)

def product_view(request):
    # Fetch product data from your desired source and organize it as a list
    context={'products':Product.objects.all()}
    return render(request, 'product.html',context)

def productdetails(request,id):
      obj1= Product.objects.get(id=id)
      context={'product':obj1}
      return render(request,'product/details.html',context)
  


# def addproduct(request):
#     if (request.method=='POST'):
#         Product.objects.create(name=request.POST['tname'],
                                
#                                 details=request.POST['tdetails'],)
#         r=reverse("product")
#         return HttpResponseRedirect(r)
#     return render(request,'add.html')
def productdelete(request,id):
       Product.objects.filter(id=id).delete()
     
       r=reverse("product")
       return HttpResponseRedirect(r)
def addformproduct(request):
      form=ProductForm()
      context={'form':form}
      if (request.method=='POST'):
            form= ProductForm(request,request.POST,request.FILES)
        
            if (form.is_valid):
                Product.objects.create(name=request.POST['name'],
                                
                                details=request.POST['details'],
                                
                                 image=request.FILES['image'],
                                 category=Category.objects.get(id=request.POST['category'],))
                                
                r=reverse("product")
                return HttpResponseRedirect(r)
            else:
                context['msg']='Data not compelete'
      return render(request,'formadd.html',context)   
  
def productupdate(request,id):
    product=Product.objects.get(id=id)
    context={'product':product}
    
    form=ProductForm()
    context={'form':form}
    if (request.method=='POST'):
         form= ProductForm(request,request.POST,request.FILES)
       
         if (form.is_valid):
             obj1=Product.objects.get(id=id)
             obj1.name=request.POST['name']
                                    
             obj1.details=request.POST['details']
             obj1.image=request.FILES['image']
             obj1.category=Category.objects.get(id=request.POST['category'])
             obj1.save()
            # Product.objects.filter(id=id).update(name=request.POST['name'],
                                    
            #                         details=request.POST['details'],
            #                          image=request.FILES['image'],
            #                                category=Category.objects.get(id=request.POST['category'],))
             r=reverse("product")
             return HttpResponseRedirect(r)
         else:
            context['msg']='please,fill all fields'
    return render(request,'product/update.html',context)