from .models import Question, Answer, Comment
from django import forms


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["subject", "content"]  # html 에 태그에 name 속성?


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
