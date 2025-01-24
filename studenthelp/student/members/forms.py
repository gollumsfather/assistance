from django import forms
from django.http import HttpResponse


class login(forms.Form):
    question=forms.CharField(label="question", max_length=255)