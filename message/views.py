from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import json
from .models import Message

@login_required
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
