from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    question_short = models.CharField(max_length=50)

    def __str__(self):
        return self.question_text


class Student(models.Model):
    name = models.CharField(max_length=1000)
    nick_name = models.CharField(max_length=1000)

    def __str__(self):
        if self.nick_name == "":
            return self.nick_name
        else:
            return self.name


# class Answer(models.Model):
#     question_id = models.ForeignKey(Question, blank=True, null=True, on_delete=models.CASCADE)
#     answer_text = models.CharField(max_length=1000)
#     student_id = models.ForeignKey(Student, blank=True, null=True, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.answer_text

