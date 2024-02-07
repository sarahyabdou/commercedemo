from django.shortcuts import render,reverse,redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms  import *
from django.views import View
from django.views.generic import UpdateView,DetailView,DeleteView,ListView,CreateView
from django.urls import reverse_lazy

class CategoryAddgeneric(CreateView):
    model=Category
    template_name='addd.html'
    form_class=CategoryForm
    success_url=reverse_lazy('category')
class CategoryListgeneric(ListView):
    model=Category
    template_name='category.html'
    context_object_name='categories'
    success_url=reverse_lazy('category')
class CategoryDeletegeneric(DeleteView):
    model=Category
    template_name='delete.html'
    success_url=reverse_lazy('category')
class CategoryDetailgeneric(DetailView):
    model=Category
    template_name='detailss.html'
    context_object_name='category'
class CategoryUpdategeneric(UpdateView):
    model=Category
    template_name='uppdate.html'
    context_object_name='form'
    success_url=reverse_lazy('category')
    form_class=CategoryForm

# def categoryupdate(request,id):
#     category=Category.objects.get(id=id)
#     context={'category':category}
    
#     form=CategoryForm()
#     context={'form':form}
#     if (request.method=='POST'):
#          form= CategoryForm(request,request.POST,request.FILES)
       
#          if (form.is_valid):
#              obj1=Category.objects.get(id=id)
#              obj1.name=request.POST['name']
                                    
#              obj1.details=request.POST['details']
#              obj1.numberproducts=request.POST['numberproducts']
#              obj1.image=request.FILES['image']
           
#              obj1.save()
        
#              r=reverse("category")
#              return HttpResponseRedirect(r)
#          else:
#             context['msg']='please,fill all fields'
#     return render(request,'category/update.html',context)
def category_view(request):
    # Fetch product data from your desired source and organize it as a list
    context={'categories':Category.Getall()}
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
# def addformcategory(request):
#       form=CategoryForm()
#       context={'form':form}
#       if (request.method=='POST'):
#             form= CategoryForm(request,request.POST,request.FILES)
        
#             if (form.is_valid):
#                 Category.objects.create(name=request.POST['name'],
                                
#                                 details=request.POST['details'],
#                                 numberproducts=request.POST['numberproducts'],
#                                  image=request.FILES['image'],
#                                 )
#                 r=reverse("category")
#                 return HttpResponseRedirect(r)
#             else:
#                 context['msg']='Data not compelete'
#       return render(request,'addform.html',context)
from django.shortcuts import render, redirect, reverse
from .forms import CategoryForm  # Assuming you have imported CategoryForm from your forms.py

def categoryadd(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('category'))  # Assuming 'category' is the name of the URL pattern for the category list view
    else:
        form = CategoryForm()  # Instantiate form without any parameters for GET requests
    context = {'form': form}
    return render(request, 'category/addd.html', context)

from django.views import View
# class CategoryUpdate(View):
#     def get (self,request,id):
#       context={'form':CategoryForm(instance=Category.getcategorydetails(id))}
#       return render(request,'category/uppdate.html',context)
#     def post(self,request,id):
#       form=CategoryForm(request.POST,instance=Category.getcategorydetails(id))
#       if (form.is_valid):
#             form.save()
#             return redirect(reverse('category'))

# def updatecategory(request,id):
      
#       context={'form':CategoryForm(instance=Category.getcategorydetails(id))}
#       if(request.method=='POST'):
#           form=CategoryForm(request.POST,instance=Category.getcategorydetails(id))
#           if (form.is_valid):
#               form.save
#               return redirect(reverse('category'))
#       return render(request,'category/uppdate.html',context)
  