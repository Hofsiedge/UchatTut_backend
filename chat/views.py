# from django.shortcuts import render
from django.http import JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth.decorators import login_required
import json

from events import Event
from .models import Chat

# Create your views here.

@login_required
def chat_list(request):
    user = request.user
    # if user.is_authenticated == False:
        # return JsonResponse({'status': 'false', 'message': 'Authentication required'}, status=401)
        
    return JsonResponse(list(map(lambda x: x.json_repr, user.chat_set.all())), safe=False)

# depth states for how many message batches to load (30 for each level)
@login_required
def chat(request, chat_id, depth=1): 
    # channel_layer = get_channel_layer()
    # async_to_sync(channel_layer.group_send)('user_0', {'type': 'event.notify'}) # FIXME
    # data = json.loads(request.body)
    source = Chat.objects.get(id=chat_id)
    return JsonResponse(list(map(lambda x: x.json_repr, source.messages.reverse())), safe=False)

