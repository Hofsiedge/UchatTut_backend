# message/services/crud.py
from ..models import Message
from ..serializers import MessageSerializer

def read(id):
    return Message.objects.get(id=id)

def create(serializer: MessageSerializer):
    if serializer.is_valid():
        serializer.save()
        return serializer
