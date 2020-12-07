from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Survey)
admin.site.register(Course)
admin.site.register(Year)
