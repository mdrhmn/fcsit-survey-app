from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):

    context = {
        'survey_list': Survey.objects.all(),
    }

    # print(Survey.objects.all().name)

    return render(request, 'index.html', context)

def about_us(request):
    return render(request, 'about_us.html')