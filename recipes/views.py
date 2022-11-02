from django.shortcuts import render


def Home(request):
    return render(request, 'recipes/home.html',context={'name': 'Daniel Tolezani Castelo'}),

# Create your views here.
