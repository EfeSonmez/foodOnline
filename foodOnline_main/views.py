from django.shortcuts import render
from django.http import HttpResponse
from . import urls

def home(request):
    return HttpResponse("Welcome to the Food Online Home Page!")