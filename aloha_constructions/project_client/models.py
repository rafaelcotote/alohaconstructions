from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length= 50, null=True)
    email = models.EmailField(max_length=70,blank=True,unique=True)
    phone = models.CharField(max_length= 15, null=True)

    def __str__(self):
        return self.name
    