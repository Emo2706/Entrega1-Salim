from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()

class Games(models.Model):

    name = models.CharField(max_length=30)
    developer = models.CharField(max_length=30)
    popularity = models.IntegerField()
    type = models.CharField(max_length=30)

class Creators(models.Model):

    username = models.CharField(max_length=30)
    platforms = models.CharField(max_length=30)
    subscriptions = models.IntegerField()    
