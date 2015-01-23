from django.http import HttpResponse
import datetime
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.shortcuts import render
import models

def home(request):
    name = request.GET.get('name')
    rating = request.GET.get('rating')
    if name is not None and rating is not None:
       # print ">...........", request.GET 
        
        count = 0
        # print "nsme.....", name
        movie_object = models.Movie.objects.get(movie_name=name)
        
        # print "dsfsd",movie_object
        rate = models.Rating(movie=movie_object, sum_rating=int(rating), rating_count=count)
        rate.save()
        # print("Movie name is: " + movie_name)
        return render(request, 'home.html', {"ratings":rate})
    else:
        
        t = models.Movie.objects.order_by('-date')
        t1 = models.Movie.objects.order_by('-added_at_time')
    return render(request, 'home.html', {"tasks":t, "tasks1":t1, })

def alltasks(request):
    
    return HttpResponse()

def get_tasks(request):
    return render(request, 'task.html', {"tasks":{}})

def tasks_pending(request):
    return render(request, 'tasks_pending.html', {"tasks":{}})

def get_details(request):
    get_movie = request.GET.get('mov_name')
    movie_detail = models.Movie.objects.filter(movie_name=get_movie)
    genre_all = models.Genre.objects.filter()
    return render(request, 'movieDetail.html', {"movie_detail":movie_detail, "genre_all":genre_all})

def search(request):
    get_movie_name = request.POST.get('search_name')
    get_movie_date = request.POST.get('year')
    print "vjhfjgkjkhvkglhl", get_movie_name
    results = models.Movie.objects.filter(Q(movie_name__icontains=get_movie_name),Q(date__icontains=get_movie_date))
    # print movie_search
    genre_all = models.Genre.objects.filter()
    return render(request, 'searchMovie.html', {"movie_search":results, "genre_all":genre_all})

