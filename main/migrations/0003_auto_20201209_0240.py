# Generated by Django 3.1.4 on 2020-12-08 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201209_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]
