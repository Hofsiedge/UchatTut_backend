# lesson/serializers.py
from rest_framework import serializers
from .models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'date', 'start_time', 'end_time',
                'tutor', 'student', 'color' ]
    
    def create(self, validated_data):
        lesson = Lesson(**validated_data)
        lesson.save()
        return lesson
