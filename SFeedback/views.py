from django.shortcuts import render,  get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from SFeedback.models import Question, Student
#
# from SFeedback.forms import AnswerForm, StudentForm, LikesForm, ExtrasForm, DislikesForm


def index(request):
    output = {'data':{'data1': 'the first one', 'data2': 'second one'}}
    template = loader.get_template('home.html')
    return HttpResponse(template.render(output, request))


def questionnaire(request):
    questions = Question.objects.all()
    output = {'questions': questions}
    template = loader.get_template('questions.html')
    return HttpResponse(template.render(output, request))
#
#
# def student_form(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             # question_obj = get_object_or_404(Question, pk=question)
#             student_name = form.cleaned_data['answer1']
#             student_nickname = form.cleaned_data['answer2']
#
#             new_student = Student(name=student_name, nick_name=student_nickname)
#             new_student.save()
#
#             request.session['student_id'] = new_student.pk
#
#             return redirect('/likes/')
#
#     else:
#         form = StudentForm()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'answer.html', context)
#
#
# def likes(request):
#     if request.method == 'POST':
#         form = LikesForm(request.POST)
#         if form.is_valid():
#             student = Student.objects.get(pk=request.session['student_id'])
#
#             question = Question.objects.get(question_short='Likes')
#             answer_response = form.cleaned_data['answer_likes']
#             new_answer = Answer(question_id=question, answer_text=answer_response, student_id=student)
#             new_answer.save()
#
#             question = Question.objects.get(question_short='WhyCS')
#             answer_response = form.cleaned_data['answer_why_CS']
#             new_answer = Answer(question_id=question, answer_text=answer_response, student_id=student)
#             new_answer.save()
#
#             question = Question.objects.get(question_short='Future')
#             answer_response = form.cleaned_data['answer_future']
#             new_answer = Answer(question_id=question, answer_text=answer_response, student_id=student)
#             new_answer.save()
#
#             return redirect('/dislikes/')
#
#     else:
#
#         form = LikesForm()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'likes.html', context)
#
#
# def dislikes(request):
#     if request.method == 'POST':
#         form = DislikesForm(request.POST)
#         if form.is_valid():
#             student = Student.objects.get(pk=request.session['student_id'])
#
#             question = Question.objects.get(question_short='NoLike')
#             answer_response = form.cleaned_data['answer_not_like']
#             new_answer = Answer(question_id=question, answer_text=answer_response, student_id=student)
#             new_answer.save()
#
#             question = Question.objects.get(question_short='NeedTo')
#             answer_response = form.cleaned_data['answer_need_to']
#             new_answer = Answer(question_id=question, answer_text=answer_response, student_id=student)
#             new_answer.save()
#
#             return redirect('/extras/')
#
#     else:
#
#         form = DislikesForm()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'likes.html', context)
#
#
# def extras(request):
#     if request.method == 'POST':
#         form = ExtrasForm(request.POST)
#         if form.is_valid():
#             student = Student.objects.get(pk=request.session['student_id'])
#
#             question = Question.objects.get(question_short='Code')
#             answer_response = form.cleaned_data['answer_code']
#             new_answer = Answer(question_id=question, answer_text=answer_response, student_id=student)
#             new_answer.save()
#
#             question = Question.objects.get(question_short='Companies')
#             answer_response = form.cleaned_data['answer_companies']
#             new_answer = Answer(question_id=question, answer_text=answer_response, student_id=student)
#             new_answer.save()
#
#             question = Question.objects.get(question_short='Twitch')
#             answer_response = form.cleaned_data['answer_twitch']
#             new_answer = Answer(question_id=question, answer_text=answer_response, student_id=student)
#             new_answer.save()
#
#             question = Question.objects.get(question_short='Streamer')
#             answer_response = form.cleaned_data['answer_streamer']
#             new_answer = Answer(question_id=question, answer_text=answer_response, student_id=student)
#             new_answer.save()
#
#     else:
#
#         form = ExtrasForm()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'likes.html', context)
#
# def answer(request):
#     if request.method == 'POST':
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             question = form.cleaned_data['question']
#             # question_obj = get_object_or_404(Question, pk=question)
#             answer = form.cleaned_data['answer']
#
#             new_answer = Answer(question_id=question, answer_text=answer)
#             new_answer.save()
#
#     else:
#         form = AnswerForm()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'answer.html', context)



# def shop(request):
#     buyers = Person.objects.all()
#     products = ProductToBuy.objects.all()
#     output = {'buyers': buyers, 'products': products}
#     template = loader.get_template('shop.html')
#     return HttpResponse(template.render(output, request))