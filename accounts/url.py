

from django.urls import path,include
from django.contrib.auth.views import *
from .views import *
urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    
    path('profile/',Myprofile,name='myprofile'),
    path('register/',Registrationform.as_view(),name='Register')
    
]














