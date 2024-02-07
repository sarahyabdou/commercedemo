from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required
# from .views import CategoryUpdate
from .views import CategoryUpdategeneric
from .views import CategoryDetailgeneric
from .views import CategoryDeletegeneric
from .views import CategoryListgeneric
from .views import CategoryAddgeneric
urlpatterns = [
    # path('', views.category_view, name='category'),
     path('', CategoryListgeneric.as_view(), name='category'),
      # path('new', views.addcategory, name='addcategory'),
      #  path('newform', views.addformcategory, name='addformcategory'),
      #  path('<int:id>',views.categorydetails,name="category.details"),
        #  path('Add/',views.categoryadd,name="category.add"), 
         path('Add/',login_required(CategoryAddgeneric.as_view()),name="category.add"),  
       
      #  path('Update/<int:id>',views.updatecategory,name="update.category"),
        # path('Update/<int:id>',CategoryUpdate.as_view(),name="update.category"),
            path('Update/<int:pk>',login_required(CategoryUpdategeneric.as_view()),name="update.category"),
            path('<int:pk>',CategoryDetailgeneric.as_view(),name="details.category"),
      # path('Delete/<int:id>',views.categorydelete,name="category.delete"),
         path('Delete/<int:pk>',login_required(CategoryDeletegeneric.as_view()),name="delete.category"),
]
