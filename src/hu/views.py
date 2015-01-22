from django.http import HttpResponse
import datetime
from hu.models import Task
from django.contrib.auth import authenticate, login
from django.shortcuts import render

def home(request):
    return HttpResponse("Home Page")

def alltasks(request):
    t = Task.objects.all()
    return HttpResponse(t)

def get_tasks(request):
    t=Task.objects.all()
    return render(request,'task.html',{"tasks":t})

def tasks_pending(request):
    t=Task.objects.filter(task_status=0)
    return render(request,'tasks_pending.html',{"tasks":t})
