from django.http import JsonResponse
from django.utils import timezone

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

import json
from .models import Message

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def message(request, id=None):
    user = request.user
    if request.method == 'GET':
        return JsonResponse(Message.objects.get(id=id).json_repr)

    if request.method == 'POST':    # write
        data = json.loads(request.body)
        message = Message(text=data.get('text', ''),
                          sender=user,
                         )
        message.save()
        return JsonResponse(message.json_repr)
    if request.method == 'PUT':     # edit
        pass
