from django.contrib import admin
from django.urls import path
from Primera import views

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('Discos/', views.Discos, name='Discos'),
]