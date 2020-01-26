# lesson/models.py
from django.db import models
from django.utils import timezone

from user.models import User

class Lesson(models.Model):
    title       = models.CharField(max_length=500)
    date        = models.DateField()
    start_time  = models.TimeField()
    end_time    = models.TimeField()   # TODO: assertion end_time > start_time
    tutor       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutor_lessons')
    student     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_lessons')
    color       = models.PositiveIntegerField()     # ARGB

    def __str__(self):
        return f'{self.title} {self.date} ({self.start_time} - {self.end_time}). {self.tutor} - {self.student}'
