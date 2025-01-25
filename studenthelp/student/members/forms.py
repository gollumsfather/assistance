from django import forms

choose =( 
    ("1", "Math"), 
    ("2", "Science"),
) 

class QuestionForm(forms.Form):
    question = forms.CharField(label="Question", max_length=255)
    typeofquestion = forms.MultipleChoiceField(label="Type of question", choices=choose)
class AnswerForm(forms.Form):
    question_id = forms.IntegerField(widget=forms.HiddenInput())
    answer = forms.CharField(label="answer", max_length=255)
class ScienceQuestionForm(forms.Form):
    question = forms.CharField(label="Question", max_length=255)
    typeofquestion = forms.MultipleChoiceField(label="Type of question", choices=choose)
class ScienceAnswerForm(forms.Form):
    question_id = forms.IntegerField(widget=forms.HiddenInput())
    answer = forms.CharField(label="answer", max_length=255)
