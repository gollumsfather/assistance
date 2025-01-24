from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import login
from django.shortcuts import render, redirect

def members(request):
  template = loader.get_template('main.html')
  currentlogin=Member.objects.all().values()
  context={
    'members':currentlogin,
    'login' : login,
    }
  return HttpResponse(template.render(context, request))

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def question(request):
  if request.method=="POST":
    form=question.post
    if form.is_valid():
        return render("home")
    else:
        form = NameForm()
        return render(request, "main.html", {"form": form})