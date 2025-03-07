from django.db import models

# Create your models here.

class Chat(models.Model):
    text = models.CharField(max_length=1000)

    class Meta:
        ordering = ['id']