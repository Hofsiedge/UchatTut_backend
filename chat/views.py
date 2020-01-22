from django.http import JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
import json

from events import Event
from . import services
import message.services

from message.serializers import MessageSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def chat_list(request):
    user = request.user
    return JsonResponse(list(map(lambda x: x.json_repr, user.chat_set.all())), safe=False)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
# depth states for how many message batches to load (30 for each level)
def chat(request, chat_id, depth=1): 

    source = services.read(id=chat_id)

    if request.method == 'GET':
        serializer = MessageSerializer(source.messages.reverse(), many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':        # send a message to the chat
        # TODO: refactor with a serializer ?
        data = json.loads(request.content)
        content_type = data.get('type', None)

        if content_type is None:
            return JsonResponse({'message': 'Missing "type" field.'}, 
                                status=400)

        if content_type == 'message':
            msg_id = data.get('msg_id', None)
            if msg_id is None:
                return JsonResponse({'message': 'Missing "msg_id" field.'}, 
                                    status=400)
            if msg_id is not int:
                return JsonResponse({'message': '"msg_id" must be an integer.'}, 
                                    status=400)
            message = message.services.read(id=msg_id)
            source.messages.add(message)
            # TODO: send notification
            # channel_layer = get_channel_layer()
            # async_to_sync(channel_layer.group_send)('user_0', {'type': 'event.notify'})
            return JsonResponse({'msg_id': 0})

        return JsonResponse({'message': 'Incorrect value of "type" field. Consider "message" type.'}, 
                            status=400)


