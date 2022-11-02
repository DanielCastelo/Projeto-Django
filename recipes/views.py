from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return HttpResponse('Teste Home')

def Sobre(request):
    return HttpResponse('Teste Sobre')

def Contato(request):
    return HttpResponse('Teste Contato')


# Create your views here.
