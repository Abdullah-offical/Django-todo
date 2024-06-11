

from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('addTask/', views.addTask, name='addTask'), 
    path('mark_as_done/<int:pk>', views.mark_as_done, name='mark_as_done'),   
    path('mark_as_not_done/<int:pk>', views.mark_as_not_done, name='mark_as_not_done'),  
    path('editTask/<int:pk>', views.editTask, name='editTask'), 
    path('deleteTask/<int:pk>', views.deleteTask, name='deleteTask'), 
]