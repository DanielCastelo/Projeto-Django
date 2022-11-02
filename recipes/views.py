from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return render(request, 'recipes/home.html')

def Contato(request):
    return render(request, 'recipes/contato.html')

def Sobre(request):
    return HttpResponse('Teste Sobre')




# Create your views here.
