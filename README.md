# FCSIT Survey App

## Introduction

This is a simple web application built to **compile all FCSIT survey forms** for **faculty courses**. For **usage of FCSIT UM undergraduate students only**.

### Problem Statements

1. **Individual survey form sharing leads to spams**
   
   Every semester, there is always going to be a period of time especially during mid-semester where students will be required to create survey forms for their group/individual assignments and dissemminate them to the public en masse through various platforms, mainly WhatsApp, Telegram and even email. Dubbed as the '**survey season**', one is expected to find their social media platforms **flooded with endless survey forms** which can sometimes lead to **spams**. This can be quite a nuisance to some especially when the same survey forms are being forwarded in as many common groups as possible to reach more people.

2. **Lack of incentive to fill survey forms**
    
    Pertaining to point #1, one of the major implications of the survey forms being shared in an unorganised and cluttered manner is that it **further disincentivises people** — which let's face it, are already generally unresponsive when it comes to filling survey forms — from doing so in the first place. 

3. **No Single Point of Reference**
    
    Due to the **lack of a single, reliable, user-friendly and easily accessible platform** to host all the survey forms, students understandably have no choice but to share their survey forms in multiple platforms in order to reach as many respondents as possible. Students are also **restricted to the target groups that they can access** (e.g. A first year student could not share their survey forms in sophomore or final year students' groups), further limiting the number of possible respondents.

### Inspirations

There are essentially **2 key reasons** that motivated me to do this side project:

1. **'*What I wish I knew as a 1st Year CS student*'** by **Desmond Yeoh**

    On the 5th of December 2020, I attended a short sharing session by one of FCSIT's prominent alumni, Desmond Yeoh. He shared some tips on what students can and should do in their early years of study. One of the recommendations include building your GitHub portfolios such as by developing stuffs that can solve real life problems. He outlined 3 benefits of doing so: **

    * You can flex your resume as interviewers **ALWAYS** ask for GitHub & portfolios
    * You get to **solve your own problems** as well as the **community**
    * You can **showcase your technical & problem solving skills**

    Soon after that, I started brainstorming on several ideas on what existing real life issues can I solve as a mini side project. Judging by this GitHub repository and the endless notifications I got from my social media platforms, you know the answer already.

2. **Cement my understanding of Django**

    This web app is built almost entirely using **Python's Django back-end framework**. I have been learning and using it extensively for months during my internship. I figured, what better way to actually **put my months worth of skills** in web development to the **test** than to **actually develop my own app**? In addition, I decided to challenge myself further by testing whether I can finish the web app in less than a week, or even a day. Hackathon-style, so to speak.

### Credits

Huge shoutouts to the following groups of people for supporting this mini side project of mine:

1. Jason Chao (my incredibly supportive internship supervisor)
2. Izzah Gani (the first person whom I pitched the idea to at 1AM)
3. Faidz Hazirah, Nadia Jamhari (my earliest beta testers)

## Technology Stack

### Front-end
* Bootstrap 4.5.3
  
### Back-end
* Django==3.1.4
    * djangorestframework==3.12.2
    * django-summernote==0.8.11.6
    * dj-database-url==0.5.0
    * django-heroku==0.3.1
* gunicorn==20.0.4
* whitenoise==5.2.0
* python-dotenv==0.15.0
* psycopg2==2.8.6
* psycopg2-binary==2.8.6
* beautifulsoup4==4.9.3
* Markdown==3.3.3

### Installing dependencies

Run the following command inside your virtual environment:

- Using **pipenv**:
    ```Shell
    $ pipenv install -r requirements.txt # (Python 2)
    $ pipenv3 install -r requirements.txt # (Python 3)
    ``` 
- Using **venv**:
    ```Shell
    $ pip install -r requirements.txt # (Python 2)
    $ pip3 install -r requirements.txt # (Python 3)
    ``` 

## Deployed Web Application

Click **[here](https://fcsit-survey-app.herokuapp.com/)** to view the **deployed web app**!

Click **[here](https://github.com/mdrhmn/fcsit-survey-app)** to visit the **GitHub repository**!

## Features


## References

1. https://fcsit-fyp-surveys.herokuapp.com/
2. https://www.codementor.io/@jamesezechukwu/how-to-deploy-django-app-on-heroku-dtsee04d4
3. https://stackoverflow.com/questions/59332225/hitting-500-error-on-django-with-debug-false-even-with-allowed-hosts
4. https://stackoverflow.com/questions/6208363/sharing-a-url-with-a-query-string-on-twitter
5. https://help.heroku.com/GDQ74SU2/django-migrations