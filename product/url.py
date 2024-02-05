from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
   
     path('', views.product_view, name='product'),
      # path('new', views.addproduct, name='addproduct'),
      path('newform', views.addformproduct, name='addformproduct'),
     path('<int:id>',views.productdetails,name="product.details"),
       path('Update<int:id>',views.productupdate,name="product.update"),
     path('Delete/<int:id>',views.productdelete,name="product.delete"),
]
