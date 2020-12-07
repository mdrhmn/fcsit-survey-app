from django.shortcuts import render
from .models import *
# Create your views here.

def main(request):
    return render(request, 'index.html')