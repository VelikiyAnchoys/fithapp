# Generated by Django 5.1.2 on 2024-11-05 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitnes_app', '0002_spectren_exercise_spectren_image_spectren_times'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spectren',
            name='exer',
        ),
        migrations.RemoveField(
            model_name='spectren',
            name='exer_one',
        ),
    ]
