from django.http import HttpResponse
import datetime
from django.contrib.auth import authenticate, login
from django.shortcuts import render

def home(request):
    return HttpResponse("Home Page")

def alltasks(request):
    
    return HttpResponse()

def get_tasks(request):
    return render(request,'task.html',{"tasks":{}})

def tasks_pending(request):
    return render(request,'tasks_pending.html',{"tasks":{}})
