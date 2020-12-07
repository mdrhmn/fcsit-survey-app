from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    year = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(3)])
    course_code = models.ForeignKey("Course", on_delete=models.CASCADE) 
    link = models.CharField(max_length=200)
    PIC_name = models.CharField(max_length=100)
    PIC_email = models.CharField(max_length=100)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Course(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(3)])

    def __str__(self):
            return self.code