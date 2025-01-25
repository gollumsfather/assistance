from django.db import models

# Create your models here.

class Question(models.Model):
    questions=models.CharField(max_length=255)
    answers = models.CharField(max_length=255)
class ScienceQuestion(models.Model):
    questions=models.CharField(max_length=255)
    answers = models.CharField(max_length=255)