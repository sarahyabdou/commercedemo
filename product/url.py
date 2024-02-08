from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.decorators import login_required
from . import views
from .views import ProductUpdategeneric
from .views import ProductDetailgeneric
from .views import ProductDeletegeneric
from .views import ProductListgeneric
from .views import ProductAddgeneric

urlpatterns = [
   
    #  path('', views.product_view, name='product'),
    path('', ProductListgeneric.as_view(), name='product'),
      # path('new', views.addproduct, name='addproduct'),
      # path('newform', views.addformproduct, name='addformproduct'),
       path('Add/',login_required(ProductAddgeneric.as_view()) , name='addformproduct'),
        
         path('Delete/<int:pk>',login_required(ProductDeletegeneric.as_view()),name="product.delete"),
           path('Update/<int:pk>',login_required(ProductUpdategeneric.as_view()),name="product.update"),
     path('<int:pk>',ProductDetailgeneric.as_view(),name="product.details"),
     path('API/',include('product.api.url'))
      #  path('Update<int:id>',views.productupdate,name="product.update"),
  
]
