import json

from django.http import JsonResponse
from django.utils import timezone

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from . import services
from .serializers import MessageSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def message(request, id=None):
    user = request.user
    if request.method == 'GET':
        serializer = MessageSerializer(services.read(id))
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':    # write
        data = json.loads(request.body)
        serializer = MessageSerializer(data={**data, 'sender': user.id})
        if serializer.is_valid():
            # TODO: refactor with serializer.save ?
            message = services.create(serializer)
            return JsonResponse(message.data, safe=False)
        else:
            return JsonResponse(serializer._errors, status=400)

    if request.method == 'PUT':     # edit
        pass
