# Generated by Django 4.2.9 on 2024-05-11 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_checkin', '0004_checkinregister_hours_worked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkinregister',
            name='type_register',
        ),
    ]
