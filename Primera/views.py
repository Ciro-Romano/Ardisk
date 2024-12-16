from django.shortcuts import render

def Inicio(request):
    return render(request, 'primera/Inicio.html')

def Discos(request):
    return render(request, 'Primera/Discos.html')
