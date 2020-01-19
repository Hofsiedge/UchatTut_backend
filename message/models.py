from django.db import models
from django.utils import timezone

from user.models import User


class Message(models.Model):
    sender  = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='messages', null=True)
    time    = models.DateTimeField(default=timezone.now)
    text    = models.CharField(max_length=500)
    # TODO: attachments
    # messages, image, file

    def __str__(self):
        return f'{self.sender} [{self.time}]: {self.text}'

    @property
    def json_repr(self):
        return {
            "id":       self.id,
            "sender":   self.sender.id,
            "time":     self.time,
            "text":     self.text,
            # TODO
            "attachments": [],
        }

