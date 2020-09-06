from django.contrib import admin
from django.urls import path
from starWarsApi import views

urlpatterns = [
    path('', views.index),
    path('planets/', views.addGetPlanets, name='planets'),
    path('planets/id/<str:planet_id>', views.getDeletePlanet, name='planetsId'),
    path('planets/name/<str:planet_name>', views.getDeletePlanet, name='planetsName'),
]
