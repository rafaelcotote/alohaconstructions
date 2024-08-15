from django.db import models
from project_client.models import Client
# Create your models here.

class CadastroProjeto(models.Model):
    project_name = models.CharField(max_length=150, null=False, blank=True, verbose_name='Project Name')
    project_description = models.TextField(null=False, blank=True, verbose_name= 'Project Description',)
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    project_adress = models.TextField(null=False, blank=True, verbose_name= 'Project Adress',)
    estimated_budget = models.IntegerField(null=True, blank=True, verbose_name= "Estimated Budget")
    total_amount_spend = models.IntegerField(null=True, blank=True, verbose_name= "Total Amount Spent")
    estimated_project_duration = models.IntegerField(null=True, blank=True, verbose_name= "Estimated Project Duration")

    def __str__(self):
        return self.project_name
    
class Task(models.Model):
    text = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    estimated_time = models.DurationField()

    def __str__(self):
        return self.text
    