from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')