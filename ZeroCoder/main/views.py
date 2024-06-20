from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'caption': "CatDjango"
    }

    return render(request,"main/index.html",data)

def lev(request):
    return render(request, "main/lev.html")

def down(request):
    return render(request, "main/down.html")

def new(request):
    return render(request, "main/new.html")


# Create your views here.
