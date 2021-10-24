from django.db import models


class Student(models.Model):
    identity_name = models.CharField(max_length=256)
    questions = models.ManyToManyField("Question", related_name="students",
                                       through="Answer")


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=32)
    create_date = models.DateTimeField(auto_now=True)
    questions = models.ImageField()


class Question(models.Model):
    question_number = models.IntegerField()
    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE, related_name="questions")
    right_ans = models.CharField(max_length=32)


class Answer(models.Model):
    student_answer = models.CharField(max_length=32)
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
