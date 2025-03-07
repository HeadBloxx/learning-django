from django.db import models

# Create your models here.

class Task(models.Model):
    text = models.CharField(max_length=50)
    priority = models.DecimalField(max_digits=1,decimal_places=0)