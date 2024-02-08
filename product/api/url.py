from django.urls import path
from .views import *
urlpatterns = [
    path('Hello',Hello,name='hello'),
    path('acceptdata/',acceptdata,name='acceptdata'),
      path('all/',all,name='all'),
      path('detail/<int:id>/',detail,name='detail'),
      path('add/',add,name='add'),
       path('update/<int:id>/',update,name='update'),
       path('delete/<int:id>/',delete,name='delete'),
       #########generic view
        path('allg/',allg.as_view(),name='allg'),
        ##based class
     path('allc/',allc.as_view(),name='allc')
]