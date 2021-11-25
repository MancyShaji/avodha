from django.urls import path
from . import views

urlpatterns=[
    path('', views.fun,name='fun'),
    path('watch', views.watch,name='watch'),
    path('add', views.add,name='add')
]    
    