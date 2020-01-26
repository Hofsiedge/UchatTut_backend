# lesson/services/crud.py
from ..models import Lesson
from ..serializers import LessonSerializer

from user.models import User

def read(id: int):
    return Lesson.objects.get(id=id)

def filter(user: User):
    if user.is_tutor:
        return Lesson.objects.filter(tutor=user.id)
    return Lesson.objects.filter(student=user.id)

def create(serializer: LessonSerializer):
    if serializer.is_valid():
        lesson = serializer.save()
        return lesson
