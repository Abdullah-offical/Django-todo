from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('employee/<int:pk>/', views.employee_details, name='employee_details')
]