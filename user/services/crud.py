from django.db.models import Q
from ..models import User

def read(id: int):
    user = User.objects.get(id=id)
    not_user = ~user.is_tutor
    return User.objects.filter(is_tutor=not_user)

def search(query, tutor):
    Qs      = [Q(name__contains=word) | Q(surname__contains=word)
             | Q(is_tutor__equals=tutor) for word in query.split()]
    users   = User.filter(*Qs)
    return users
