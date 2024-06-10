from django.shortcuts import render, HttpResponse

def todo(request):
    return render(request, 'todo.html')
    # return HttpResponse("Todo")
