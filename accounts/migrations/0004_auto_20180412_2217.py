# Generated by Django 2.0.3 on 2018-04-12 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180412_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='College',
        ),
        migrations.AddField(
            model_name='profile',
            name='college',
            field=models.CharField(blank=True, choices=[['DJ Sanjvi', 'DJ Sanjvi'], ['Folo', 'Folo'], ['Fr. Bandra', 'Fr. Bandra'], ['Loking', 'Loking'], ['VIT', 'VIT']], max_length=30),
        ),
    ]
