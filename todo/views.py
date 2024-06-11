from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Task

def todo(request):
    # use filter for get multiple filesd use conditions 
    task = Task.objects.filter(is_complete=False)
    completed_task = Task.objects.filter(is_complete=True)
    context = {
        'task' : task,
        'completed_task' : completed_task,
    }
    return render(request, 'todo.html', context)
    # return HttpResponse("Todo")

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task = task).order_by('updated_at')
    return redirect('todo')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk) # task is exsist or not not to show 404
    task.is_complete = True
    task.save()
    return redirect('todo')

def mark_as_not_done(request, pk):
    task = get_object_or_404(Task, pk=pk) 
    task.is_complete = False
    task.save()
    return redirect('todo')

def editTask(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('todo')
    else: # page refresh or come frist time
        context = {
            'get_task': get_task,
        }
        return render(request, 'editTask.html', context);
    
def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('todo')