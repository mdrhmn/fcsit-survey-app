from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    # path('about_us/', views.about_us, name='about_us'),
    path('whatsapp_api/', views.whatsapp_api, name='whatsapp_api'),
    path('twitter_api/', views.twitter_api, name='twitter_api'),

]