from django.db import models
from django.utils import timezone

from user.models import User
from message.models import Message


class Chat(models.Model):
    users   = models.ManyToManyField(User, related_name="chats")
    name    = models.CharField(max_length=50)
    messages = models.ManyToManyField(Message, related_name='+')

    def __str__(self):
        return f'{self.name}: ' + '; '.join(map(str, users))

    @property
    def json_repr(self):
        return {
            "id":       self.id,
            "users":    [user.id for user in users],
            "name":     self.name,
        }
