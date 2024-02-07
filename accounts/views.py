from django.shortcuts import render,redirect,reverse
from django.urls import reverse_lazy
from django.contrib.auth.forms import authenticate
from product .models import *

from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# def Mylogin(request):
#     context={'form':authenticate()}
#     return render(request,'registration/login',context)
def Myprofile(request):
    
    return redirect(reverse('product'))
class Registrationform(CreateView):
    model=User
    template_name='registration/register.html'
    form_class= UserCreationForm
    context_object_name='form'
    success_url=reverse_lazy('login')
    
# Create your views here.
