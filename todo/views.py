from django.shortcuts import redirect, render, HttpResponse
from .models import Task

def todo(request):
    # use filter for get multiple filesd use conditions 
    task = Task.objects.filter(is_complete=False)
    context = {
        'task' : task,
    }
    return render(request, 'todo.html', context)
    # return HttpResponse("Todo")

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task = task).order_by('updated_at')
    return redirect('todo')
