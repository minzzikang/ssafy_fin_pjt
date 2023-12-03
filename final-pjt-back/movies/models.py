from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class Director(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class Movie(models.Model):
    actors = models.ManyToManyField(Actor)
    adult = models.BooleanField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    id = models.IntegerField(primary_key=True)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    runtime = models.IntegerField()
    trailer_key = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    movie_like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='user_like_movies', blank=True
    )

class Moviecomment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=20)
    rating = models.IntegerField()
