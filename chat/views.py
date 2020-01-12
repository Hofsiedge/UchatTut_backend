# from django.shortcuts import render
from django.http import JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from events import Event

# Create your views here.

def chat_list(request):
    return JsonResponse([
        {"id": 1, "name": "", "users": [0, 1]},
        {"id": 2, "name": "", "users": [0, 2]},
        {"id": 3, "name": "Chat #", "users": [0, 1, 2]},
    ], safe=False) # safe=True only allows to send dicts

# depth states for how many message batches to load (30 for each level)
def chat(request, chat_id, depth=1): 
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('user_0', {'type': 'event.notify'}) # FIXME
    return JsonResponse([], safe=False)

