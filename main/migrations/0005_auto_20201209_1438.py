# Generated by Django 3.1.4 on 2020-12-09 06:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_survey_date_applied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='date_applied',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
