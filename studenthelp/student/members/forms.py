from django import forms

choose =( 
    ("1", "Math"), 
    ("2", "Science"), 
    ("3", "English"), 
    ("4", "Social Studies"), 
) 

class QuestionForm(forms.Form):
    question = forms.CharField(label="Your Question", max_length=100)
    typeofquestion = forms.MultipleChoiceField(label="Type of question", choices=choose)

class AnswerForm(forms.Form):
    answer = forms.CharField(label="answer", max_length=255)