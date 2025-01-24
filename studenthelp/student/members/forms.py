from django import forms

choose =( 
    ("1", "Math"), 
    ("2", "Science"), 
    ("3", "English"), 
    ("4", "Social Studies"), 
) 

class QuestionForm(forms.Form):
    question = forms.CharField(label="Your Question", max_length=100)
    typeofquestion = forms.MultipleChoiceField(label="type of question", choices=choose)
