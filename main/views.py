from django.shortcuts import redirect, render
import re
from .models import *
from django.contrib import messages
import urllib.parse
# Create your views here.

def home(request):

    if request.method == 'POST':
        # regex = re.compile('[@!#$%^&*()<>?/\|}{~:]')
        title = request.POST['title'].strip()
        description = request.POST['description']
        year = Year.objects.get(year=int(request.POST['year']))
        course_code = Course.objects.get(code=request.POST['course_code'])
        link = request.POST['link']
        PIC_name = request.POST['PIC_name']
        PIC_email = request.POST['PIC_email']

        new_survey = Survey(
            title=title,
            description=description,
            year=year,
            course_code=course_code,
            link=link,
            PIC_name=PIC_name,
            PIC_email=PIC_email,
        )

        # Save ticket changes
        new_survey.save()

        messages.success(
                request, "Survey form application successful")

    context = {
        'survey_list': Survey.objects.all(),
        'course_list': Course.objects.all(),
        'y1_course_list': Course.objects.filter(year__year=1),
        'y2_course_list': Course.objects.filter(year__year=2),
        'y3_course_list': Course.objects.filter(year__year=3),
        'year_list': Year.objects.all(),
    }

    return render(request, 'home.html', context)

def about_us(request):
    return render(request, 'about_us.html')

def whatsapp_api(request):
    text = request.POST['title'] + '\n\n' + request.POST['description'] + '\n\n' + request.POST['survey_link']
    link = urllib.parse.quote(text)
    return redirect('https://api.whatsapp.com/send?phone=&text=' + link)
    