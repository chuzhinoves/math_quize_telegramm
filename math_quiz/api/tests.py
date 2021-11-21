from django.test import TestCase

from .models import Quiz
from .serializers import QuizSerializer

# Create your tests here.
class test_db(TestCase):
    def test_quiz_create(self):
        data = {'quiz_name' : 'lion'}
        quiz_serizlizer = QuizSerializer(data=data)
        quiz_serizlizer.is_valid()
        quiz_serizlizer.save()
        lion = Quiz.objects.get(quiz_name='lion')
        self.assertEqual(lion.quiz_name, 'lion')