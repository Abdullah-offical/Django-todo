from django.http import Http404
from django.shortcuts import render, HttpResponse
from .models import Employee

# Create your views here.
def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})
    # return HttpResponse("Hello World")

def employee_details(request, pk):
    try:
        employess = Employee.objects.get(pk=pk)
        context = {
            'employess' : employess,
        }
        return render(request, 'employee_details.html', context)
    except:
        raise Http404
