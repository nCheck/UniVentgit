# Generated by Django 2.0.3 on 2018-04-12 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventPosts', '0002_post_posted_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='event_date',
        ),
    ]
