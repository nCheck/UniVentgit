# Generated by Django 2.0.3 on 2018-03-18 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_college_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='slug',
            field=models.SlugField(default='hello', unique=True),
        ),
    ]
