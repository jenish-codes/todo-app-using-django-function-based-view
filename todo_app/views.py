from django.shortcuts import redirect, render
from .models import Tasks

def home(request):
    tasks = Tasks.objects.all()
    return render(request, "todo_app/index.html", {'tasks':tasks})

def addtask(request):
    task = request.POST.get('task')
    tasks = Tasks(task=task)
    tasks.save()
    return redirect('home')

def deletetask(request, pk):
    task = Tasks.objects.get(pk=pk)
    task.delete()
    return redirect('home')

def update(request,pk):
    task = Tasks.objects.get(pk=pk)
    return render(request, "todo_app/update.html",{'task':task})

def updatetask(request, pk):
    t = request.POST.get('task')
    tasks = Tasks.objects.get(pk=pk)
    tasks.task = t
    tasks.save()
    return redirect('home')