from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from typing import List

from App1.forms import CreatorsForm, GamesForm, UserForm
from App1.models import Creators, Games, User

# Create your views here.

def inicio(request):

      return render(request, "App1/inicio.html")

def users(request):

      if request.method == 'POST':

            Formulario1 = UserForm(request.POST)

            print(Formulario1)

            if Formulario1.is_valid: 

                  data = Formulario1.cleaned_data

                  user = User(name=data['name'], city=data['city'], age=data['age'], email=data['email']) 

                  user.save()

                  return render(request, "App1/inicio.html")

      else: 

            Formulario1 = UserForm()

      return render(request, "App1/users.html", {"Formulario1":Formulario1})

def games(request):

      if request.method == 'POST':

            Formulario2 = GamesForm(request.POST)

            print(Formulario2)

            if Formulario2.is_valid: 

                  data = Formulario2.cleaned_data

                  games = Games(name=data['name'], developer=data['developer'], popularity=data['popularity'], type=data['type']) 

                  games.save()

                  return render(request, "App1/inicio.html")

      else: 

            Formulario2 = GamesForm()

      return render(request, "App1/games.html", {"Formulario2":Formulario2})

def creators(request):

      if request.method == 'POST':

            Formulario3 = CreatorsForm(request.POST)

            print(Formulario3)

            if Formulario3.is_valid: 

                  data = Formulario3.cleaned_data

                  creators = Creators(username=data['username'], platforms=data['platforms'], subscriptions=data['subscriptions']) 

                  creators.save()

                  return render(request, "App1/inicio.html")

      else: 

            Formulario3 = CreatorsForm()

      return render(request, "App1/creators.html", {"Formulario3":Formulario3})

def browsingGames(request):
    return render(request, "App1/browsingGames.html")      

def search(request):

    if request.GET["name"]:

        name = request.GET['name']

        games = Games.objects.filter(name__icontains=name)
    
        return render(request, "App1/search.html", {"games":games, "name":name})

    else:

        answer = "No data sent"
        
    return render(request, "App1/inicio.html", {"answer":answer})                  