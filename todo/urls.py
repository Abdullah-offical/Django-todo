

from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('addTask/', views.addTask, name='addTask'),    
]