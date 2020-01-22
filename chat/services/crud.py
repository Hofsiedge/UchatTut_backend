from django.db.models import Q
from ..models import Chat

def read(id: int):
    return Chat.objects.get(id=id)
