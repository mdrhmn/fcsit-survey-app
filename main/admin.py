from django.contrib import admin

# Register your models here.
from .models import *
from django_summernote.admin import SummernoteModelAdmin
from .models import *

class DescriptionAdmin(SummernoteModelAdmin):
	summernote_fields = ('description',)
    
# admin.site.register(Survey, DescriptionAdmin)
# admin.site.register(Course)
admin.site.register(Year)

@admin.register(Survey)
class Survey(DescriptionAdmin):
    list_display = ('title', 'id', 'year', 'course_code', 'get_course_name', 'link', 'approved')
    list_filter = ('course_code', 'year')
    # ordering = ("district_name",)

    def get_course_name(self, obj):
        return obj.course_code.name
    get_course_name.short_description = 'Course Name'  # Renames column head

    def get_name(self, obj):
        return obj.title

@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ('code', 'name', 'year')
    list_filter = ('year', )
    ordering = ("year",)

    def get_name(self, obj):
        return obj.name