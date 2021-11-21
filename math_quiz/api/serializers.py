from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Quiz

class QuizSerializer (serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['quiz_name', 'create_date', 'task_img']