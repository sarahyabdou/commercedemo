from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.category_view, name='category'),
    
      path('new', views.addcategory, name='addcategory'),
     path('<int:id>',views.categorydetails,name="category.details"), 
      path('Delete/<int:id>',views.categorydelete,name="category.delete"),
]
