from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, ScienceQuestion
from .forms import AnswerForm, QuestionForm, ScienceAnswerForm, ScienceQuestionForm
from django.shortcuts import render, redirect, get_object_or_404

def members(request):
  template = loader.get_template('main.html')
  question=Question.objects.all().values()
  context={
     'questions':question
  }
  return HttpResponse(template.render())

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def question_view(request):
    questions=Question.objects.all()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            questio = form.cleaned_data['question']
            subject = form.cleaned_data['typeofquestion']
            print(subject)
            if subject==['1']:
              questy = Question(questions=questio)
              questy.save()
              return HttpResponseRedirect("/math/")
            if subject==['2']:
              questy = ScienceQuestion(questions=questio)
              questy.save()
    else:
        form = QuestionForm()

    return render(request, "main.html", {"form": form, "questions":questions})

def answer_view(request):
    questions = Question.objects.all()  # Fetch all questions

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            # Update the answer for the specified question
            question_id = form.cleaned_data['question_id']
            new_answer = form.cleaned_data['answer']

            question = get_object_or_404(Question, id=question_id)
            question.answers = new_answer
            question.save()
            print(f"Updated Question ID {question_id} with Answer: {new_answer}")
    else:
        form = AnswerForm()

    return render(request, "math.html", {"questions": questions, "form": form})

def science_answer_view(request):
    questions = ScienceQuestion.objects.all()  # Fetch all questions

    if request.method == "POST":
        form = ScienceAnswerForm(request.POST)
        if form.is_valid():
            # Update the answer for the specified question
            question_id = form.cleaned_data['question_id']
            new_answer = form.cleaned_data['answer']

            question = get_object_or_404(Question, id=question_id)
            question.answers = new_answer
            question.save()
            print(f"Updated Question ID {question_id} with Answer: {new_answer}")
    else:
        form = AnswerForm()

    return render(request, "science.html", {"questions": questions, "form": form})
