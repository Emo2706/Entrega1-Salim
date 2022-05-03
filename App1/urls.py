from django.urls import path

from App1 import views

urlpatterns = [
   
    path("", views.inicio, name="Inicio"),
    path("users/", views.users, name="Users"),
    path("games/", views.games, name="Games"),
    path("creators/", views.creators, name="Creators"),
    path('browsingGames/', views.browsingGames, name='BrowsingGames'),
    path('search/', views.search),
]