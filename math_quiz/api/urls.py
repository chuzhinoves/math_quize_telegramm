from django.urls import path, include
from rest_framework import routers

from api.views import QuizViewSet

router = routers.DefaultRouter()
router.register(r'quiz', QuizViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]