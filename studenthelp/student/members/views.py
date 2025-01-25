from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import question
from .forms import QuestionForm, AnswerForm
from django.shortcuts import render, redirect
import sqlite3

def members(request):
  template = loader.get_template('main.html')
  qestons=question.objects.all().values()
  context={
     'questions':qestons
  }
  return HttpResponse(template.render())

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def question_view(request):
    qestons=question.objects.all().values()
    context={
     'questions':qestons
    }
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            questio = form.cleaned_data['question']
            subject = form.cleaned_data['typeofquestion']
            print(subject)
            if subject==['1']:
              question = question(questions=questio[0])
              question.save()
              return HttpResponseRedirect("/math/")
            if subject==['2']:
              return HttpResponseRedirect("/science/")
            if subject==['3']:
              return HttpResponseRedirect("/english/")
            if subject==['4']:
              return HttpResponseRedirect("/socialstudies/")
    else:
        form = QuestionForm()

    return render(request, "main.html", {"form": form})

def answer_view(request):
    qestons=question.objects.all().values()
    context={
     'questions':qestons,
    }
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answeo = form.cleaned_data['answer']
            print(answeo)
    else:
        form = AnswerForm()

    return render(request, "main.html", {"form": form})