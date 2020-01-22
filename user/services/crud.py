from django.db.models import Q
from ..models import User

def read(id: int):
    return Chat.objects.get(id=id)

def search(query):
    Qs      = [Q(name__contains=word) | Q(surname__contains=word) for word in query.split()]
    users   = User.filter(*Qs)
