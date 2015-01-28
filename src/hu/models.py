from django.db import models
from django.contrib.auth.models import User
 
TASK_STATUS = ((0, "Pending"),
               (1, "Completed"))

    
class Genre(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)
    
class Director(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)
    
class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    date = models.DateField()
    genre = models.ManyToManyField(Genre)
    added_at_time = models.DateTimeField()
    added_by_user = models.ForeignKey(User)
    director = models.ForeignKey(Director)
    def __str__(self):              # __unicode__ on Python 2
        return self.movie_name

    class Meta:
        ordering = ('movie_name',)
        unique_together = (('movie_name','date'),)
        
class Rating(models.Model):
    movie = models.ForeignKey(Movie)
    rating_count = models.IntegerField()
    sum_rating = models.IntegerField()
    def __str__(self):              # __unicode__ on Python 2
        return self.movie

    class Meta:
        ordering = ('movie',)
