# FCSIT Survey App

## Introduction

This is a simple web application built to **compile all FCSIT survey forms** for **faculty courses**. For **usage of FCSIT UM undergraduate students only**.
<br>

### Problem Statements

1. **Individual survey form sharing leads to spams**
   
   Every semester, there is always going to be a period of time especially during mid-semester where students will be required to create survey forms for their group/individual assignments and dissemminate them to the public en masse through various platforms, mainly WhatsApp, Telegram and even email. Dubbed as the '**survey season**', one is expected to find their social media platforms **flooded with endless survey forms** which can sometimes lead to **spams**. This can be quite a nuisance to some especially when the same survey forms are being forwarded in as many common groups as possible to reach more people.

2. **Lack of incentive to fill survey forms**
    
    Pertaining to point #1, one of the major implications of the survey forms being shared in an unorganised and cluttered manner is that it **further disincentivises people** — which let's face it, are already generally unresponsive when it comes to filling survey forms — from doing so in the first place. 

3. **No Single Point of Reference**
    
    Due to the **lack of a single, reliable, user-friendly and easily accessible platform** to host all the survey forms, students understandably have no choice but to share their survey forms in multiple platforms in order to reach as many respondents as possible. Students are also **restricted to the target groups that they can access** (e.g. A first year student could not share their survey forms in sophomore or final year students' groups), further limiting the number of possible respondents.
<br>

### Inspirations

There are essentially **3 key reasons** that motivated me to do this side project:

1. **'*What I wish I knew as a 1st Year CS student*'** by **Desmond Yeoh**

    On the 5th of December 2020, I attended a short sharing session by one of FCSIT's prominent alumni, Desmond Yeoh. He shared some tips on what students can and should do in their early years of study. One of the recommendations include building your GitHub portfolios such as by developing stuffs that can solve real life problems. He outlined **3 benefits** of doing so:

    * You can flex your resume as interviewers **ALWAYS** ask for GitHub & portfolios
    * You get to **solve your own problems** as well as the **community**
    * You can **showcase your technical & problem solving skills**

    Soon after that, I started brainstorming on several ideas on what existing real life issues can I solve as a mini side project. Judging by this GitHub repository and the endless notifications I got from my social media platforms, you know the answer already.

2. **Improve existing FCSIT FYP Survey web app**

    Full disclaimer: **This idea is not originally mine**, at least at its most fundamentals. Earlier this year, two of my seniors Jia Xiong and Chun Wah developed a **[simple React web app ](https://fcsit-fyp-surveys.herokuapp.com/)** to compile all FYP survey forms. It was not properly advertised (I was among the few who found it lying somewhere inside SiswaMail). Nevertheless, the concept of hosting the survey forms in one place intrigued me, and I decided to expand the idea by collecting not just FYP survey forms, but also for other courses and years as well.

3. **Cement my understanding of Django**

    This web app is built almost entirely using **Python's Django back-end framework**. I have been learning and using it extensively for months during my internship. I figured, what better way to actually **put my months worth of skills** in web development to the **test** than to **actually develop my own app**? In addition, I decided to challenge myself further by testing whether I can finish the web app in less than a week, or even a day. Hackathon-style, so to speak.
<br>

### Credits

Huge shoutouts to the following groups of people for supporting this mini side project of mine:

1. **Jason Chao** (my incredibly supportive internship supervisor)
2. **Izzah Gani** (the first person whom I pitched the idea to at 1AM)
3. **Faidz Hazirah**, **Nadia Jamhari** (my earliest beta testers)

<hr>

## Technology Stack

### Front-end
* Bootstrap 4.5.3
* Bootstrap-Select 1.13.14
* Summernote 0.8.18
  
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
<hr>

## Deployed Web Application

Click **[here](https://fcsit-survey-app.herokuapp.com/)** to view the **deployed web app**!

Click **[here](https://github.com/mdrhmn/fcsit-survey-app)** to visit the **GitHub repository**!
<hr>

## Features

### 1. Add Your Surveys!

This simple web app is — well — *incredibly simple*. It is a **single-page application (SPA)** so users will not have to worry about navigations etc.

Right at the top, users can clearly see the call-to-action (CTA) 'Add my survey' button, which when clicked, will **open a modal form** that allows them to **fill in the details of their surveys**:

![hippo](https://media.giphy.com/media/akTooS0d0jH7b9jb1F/giphy.gif)

Survey forms are also **unapproved by default**, and will **only appear on the web app** after **approval from the administrator**. This is to ensure that each survey form is **thoroughly inspected** and to **avoid spams or malicious contents**.
<br><br>

### 2. WYSIWYG/Rich Text Editor Integration

Although incredibly simple at its core, the web app supports a wide range of functionalities. Users can easily customise your survey descriptions using:

1. **Basic markdowns** (e.g. bold, italic, underline)
2. **Text-formatting** (e.g. font-size, line-height, paragraph)
3. **Image attachment** (yes, you can attach photos too!)

![hippo](https://media.giphy.com/media/7jpmYafnK6EfOUQv4h/giphy.gif)
<br><br>

### 3. Dependent Dropdowns

Users do not have to worry about searching for their courses, as the **Year and Course Code dropdowns are inter-linked**. Selecting the year will **automatically filter the courses available** in that year.

![hippo](https://media.giphy.com/media/QLD8uIlJZqMvxl1wI0/giphy.gif)
<br><br>

### 4. Expiry Date

One distinct feature for this web app is that users can **set the expiry date** for their survey forms, giving them the ability to restrict how long they want their survey forms to be displayed in the web app. If users are uncertain on the expiry date, the system will **automatically set the expiry date** to **1 month from date of application**. **Credits to Faidz for suggesting this feature to me!**

<br><br>

### 5. User-friendly Navigations

Using only simple Bootstrap tabs and pills navigation, users can **browse the surveys easily** with only a few clicks! The left-side pills refer to the **years of study** while the upper-tabs refer to the **individual courses** for each year. Users can also hover over each course code tab to see the course name (handy for those who wants to know the course name without having to click the tab itself).

![hippo](https://media.giphy.com/media/tk7RUAKxZrWNTW37rL/giphy.gif)

Under each course tab, there is the **course title** as well as a **search bar**, which users can use to **search for surveys** based on their **title**, **description** and/or **PIC name**. The survey panels will adjust dynamically based on the search input. **Credits to Izzah for suggesting this feature to me!**

![hippo](https://media.giphy.com/media/cUZnT1e9MQK93kiYEZ/giphy.gif)

The survey forms are displayed in **Bootstrap accordion/collapse**. The panel header consists of the **survey title**, **expiry date**, **link** and **share dropdown**. Clicking the link will open a new tab, which will redirect you to the survey form itself.

Users can click on each accordion panel to expand its content, which contains the **PIC name**, **email** and **description**. You can only expand the content of the survey panel **one at a time** to ensure that the accordion is not cluttered.<br><br>

![hippo](https://media.giphy.com/media/PRzj8sdHLPe7HzoJjJ/giphy.gif)

### 6. Share to Various platforms

This is my most favourite feature of all! When users **click on the ellipsis '...' button** at the right side of the survey panel, a **dropdown menu** will appear, listing the 3 ways to share their survey forms:

1. **Share to WhatsApp**

    Thanks to WhatsApp API, users can forward the survey forms to their WhatsApp contacts/groups. Users will be prompted to open their WhatsApp Web client and select which groups of people to forward the survey to.

    ![hippo](https://media.giphy.com/media/pSC4z0dKBXD55emXmw/giphy.gif)

2. **Share to Twitter**

    Twitter's Tweet Web Intent API allows users to also share the survey forms via tweet. Users will be prompted to log into their Twitter account if they haven't before posting the tweet.

    ![hippo](https://media.giphy.com/media/Y2faW4w3WBdbWcoRav/giphy.gif)

3. **Share to Email**

    Last but not least, users can also share their survey forms via email. By default, the web app will include **student-info (student_info-list@siswa.um.edu.my)** and **FSKTM STUDENT - UG (fsktm_student-list@um.edu.my)** as recipients, and **attach** the **survey's title**, **description** and **link** as subject and body respectively. 

    ![hippo](https://media.giphy.com/media/L06cgLvmHahWChWtco/giphy.gif)
<br><br>

### 7. Admin Dashboard

This last feature is strictly for **administrators access only**. With Django's built-in admin dashboard, administrators can **directly access the dashboard** by clicking the Admin link at the navigation bar. 

## References

1. https://fcsit-fyp-surveys.herokuapp.com/
2. https://www.codementor.io/@jamesezechukwu/how-to-deploy-django-app-on-heroku-dtsee04d4
3. https://stackoverflow.com/questions/59332225/hitting-500-error-on-django-with-debug-false-even-with-allowed-hosts
4. https://stackoverflow.com/questions/6208363/sharing-a-url-with-a-query-string-on-twitter
5. https://help.heroku.com/GDQ74SU2/django-migrations
6. https://developer.twitter.com/en/docs/twitter-for-websites/web-intents/overview