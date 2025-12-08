from django.shortcuts import render
from django.http import HttpResponse
from . import urls

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')   