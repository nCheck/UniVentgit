# Generated by Django 2.0.3 on 2018-04-13 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180412_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='college_name',
            field=models.CharField(blank=True, choices=[['DJ Sanjvi', 'DJ Sanjvi'], ['Folo', 'Folo'], ['Fr. Bandra', 'Fr. Bandra'], ['IIT', 'IIT'], ['Loking', 'Loking'], ['VIT', 'VIT'], ['pagal khaana', 'pagal khaana']], max_length=30),
        ),
    ]
