from django.http import HttpResponse
import datetime
from django.contrib.auth import authenticate, login
from django.shortcuts import render
import models

def home(request):
    t = models.Movie.objects.order_by('-date')
    t1 = models.Movie.objects.order_by('-added_at_time')
    return render(request,'home.html',{"tasks":t,"tasks1":t1})

def alltasks(request):
    
    return HttpResponse()

def get_tasks(request):
    return render(request,'task.html',{"tasks":{}})

def tasks_pending(request):
    return render(request,'tasks_pending.html',{"tasks":{}})
