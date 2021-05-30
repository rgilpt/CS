from django import forms
from SFeedback.models import Question


class AnswerForm(forms.Form):
    question = forms.ModelChoiceField(queryset=Question.objects.all())
    answer = forms.CharField(max_length=1000)


class StudentForm(forms.Form):
    answer1 = forms.CharField(label="What's your name?", max_length=1000)
    answer2 = forms.CharField(label="What's your nickname? (Optional)", max_length=1000)


class LikesForm(forms.Form):
    question = Question.objects.get(question_short='Likes')
    answer_likes = forms.CharField(label=question, max_length=1000)
    question = Question.objects.get(question_short='WhyCS')
    answer_why_CS = forms.CharField(label=question, max_length=1000)
    question = Question.objects.get(question_short='Future')
    answer_future = forms.CharField(label=question, max_length=1000)


class DislikesForm(forms.Form):
    question = Question.objects.get(question_short='NoLike')
    answer_not_like = forms.CharField(label=question, max_length=1000)
    question = Question.objects.get(question_short='NeedTo')
    answer_need_to = forms.CharField(label=question, max_length=1000)


class ExtrasForm(forms.Form):
    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )
    question = Question.objects.get(question_short='Code')
    answer_code = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, label=question,
                              initial='', widget=forms.Select(), required=True)
    question = Question.objects.get(question_short='Companies')
    answer_companies = forms.CharField(label=question, max_length=1000)
    question = Question.objects.get(question_short='Twitch')
    answer_twitch = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, label=question,
                              initial='', widget=forms.Select(), required=True)
    question = Question.objects.get(question_short='Streamer')
    answer_streamer = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, label=question,
                              initial='', widget=forms.Select(), required=True)
