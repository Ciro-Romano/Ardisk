from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def Inicio(request):
    return render(request, 'primera/Inicio.html')

def Discos(request):
    return render(request, 'Primera/Discos.html')

def Contacto(request):
    return render(request, 'Primera/Contacto.html')
