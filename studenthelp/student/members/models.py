from django.db import models

# Create your models here.

class question(models.Model):
    questions=models.CharField(max_length=255)
    answers=models.CharField(max_length=255)