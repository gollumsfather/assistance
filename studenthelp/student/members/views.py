from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member
from .forms import QuestionForm
from django.shortcuts import render, redirect

def members(request):
  template = loader.get_template('main.html')
  currentlogin=Member.objects.all().values()
  context={
    'members':currentlogin,
    }
  return HttpResponse(template.render(context, request))

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def question_view(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            questio = form.cleaned_data['question']
            return HttpResponseRedirect(f"/home/?question={questio}")
    else:
        form = QuestionForm()

    return render(request, "main.html", {"form": form})