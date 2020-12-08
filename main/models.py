from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    year = models.ForeignKey("Year", on_delete=models.CASCADE) 
    course_code = models.ForeignKey("Course", on_delete=models.CASCADE) 
    link = models.CharField(max_length=200)
    PIC_name = models.CharField(max_length=100)
    PIC_email = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)
    expiry_date = models.DateField(default=datetime.date.today() + datetime.timedelta(days=30))
    expired = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Course(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    year = models.ForeignKey("Year", on_delete=models.CASCADE) 

    def __str__(self):
            return self.code

class Year(models.Model):
    year = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(3)])
    label = models.CharField(max_length=50)

    def __str__(self):
            return self.label