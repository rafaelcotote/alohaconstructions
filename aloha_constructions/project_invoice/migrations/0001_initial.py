# Generated by Django 4.2.9 on 2024-06-20 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255, verbose_name='Client Name')),
                ('invoice_number', models.CharField(max_length=50, unique=True, verbose_name='Invoice Number')),
                ('date', models.DateField(verbose_name='Date')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Amount')),
                ('project_name', models.CharField(max_length=255, verbose_name='Project Name')),
                ('project_description', models.TextField(verbose_name='Project Description')),
                ('project_address', models.CharField(max_length=255, verbose_name='Project Address')),
                ('estimated_budget', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Estimated Budget')),
                ('total_amount_spent', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Amount Spent')),
                ('estimated_project_duration', models.IntegerField(verbose_name='Estimated Project Duration')),
            ],
        ),
    ]
