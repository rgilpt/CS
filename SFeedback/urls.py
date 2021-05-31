from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('questions/', views.questionnaire, name='questionnaire'),
    path('answers/', views.answer, name='answer'),
    path('student/', views.student_form, name='student'),
    path('dislikes/', views.dislikes, name='dislikes'),
    path('extras/', views.extras, name='extras'),
    path('likes/', views.likes, name='likes')
]