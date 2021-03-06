from django.shortcuts import redirect, render
import re
from .models import *
from django.contrib import messages
import urllib.parse
import datetime
from bs4 import BeautifulSoup
from markdown import markdown
from django.utils import timezone
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

        if request.POST.get('expiry_date') != None and request.POST.get('expiry_date') != "" :
            expiry_date = request.POST['expiry_date']
        else:
            expiry_date = datetime.date.today() + datetime.timedelta(days=30)

        new_survey = Survey(
            title=title,
            description=description,
            year=year,
            course_code=course_code,
            link=link,
            PIC_name=PIC_name,
            PIC_email=PIC_email,
            expiry_date=expiry_date,
        )

        # Save ticket changes
        new_survey.save()

        messages.success(
                request, "Survey form application successful. Your form will appear on the website upon approval.")

        return redirect('home')

    description_set = Survey.objects.values('id', 'description', 'link')

    for desc in description_set:
        html = markdown(desc['description'])

        # remove code snippets
        html = re.sub(r'<pre>(.*?)</pre>', ' ', html)
        html = re.sub(r'<code>(.*?)</code >', ' ', html)

        # extract text
        soup = BeautifulSoup(html, "html.parser")
        text = ''.join(soup.findAll(text=True))

        desc['description'] = text

    description_filtered = description_set

    context = {
        'current_date': datetime.date.today(),
        'description_filtered': description_filtered,
        'survey_list': Survey.objects.all(),
        'course_list': Course.objects.all(),
        'y1_course_list': Course.objects.filter(year__year=1),
        'y2_course_list': Course.objects.filter(year__year=2),
        'y3_course_list': Course.objects.filter(year__year=3),
        'year_list': Year.objects.all(),
    }

    return render(request, 'home.html', context)

# def about_us(request):
#     return render(request, 'about_us.html')

def whatsapp_api(request):
    markdown_string = request.POST['title'] + '\n\n' + request.POST['description'] + '\n\n' + request.POST['survey_link']

    # md -> html -> text since BeautifulSoup can extract text cleanly
    html = markdown(markdown_string)

    # remove code snippets
    html = re.sub(r'<pre>(.*?)</pre>', ' ', html)
    html = re.sub(r'<code>(.*?)</code >', ' ', html)

    # extract text
    soup = BeautifulSoup(html, "html.parser")
    text = ''.join(soup.findAll(text=True))

    # print(text)

    link = urllib.parse.quote(text)
    return redirect('https://api.whatsapp.com/send?phone=&text=' + link)
    
def twitter_api(request):
    markdown_string = request.POST['title'] + '\n\n' + request.POST['description'] + '\n\n' + request.POST['survey_link']

    # md -> html -> text since BeautifulSoup can extract text cleanly
    html = markdown(markdown_string)

    # remove code snippets
    html = re.sub(r'<pre>(.*?)</pre>', ' ', html)
    html = re.sub(r'<code>(.*?)</code >', ' ', html)

    # extract text
    soup = BeautifulSoup(html, "html.parser")
    text = ''.join(soup.findAll(text=True))

    # print(text)

    link = urllib.parse.quote(text)
    return redirect('https://twitter.com/intent/tweet?text=' + link)
    