import json

from django.http import JsonResponse
from django.utils import timezone

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from . import services
from .serializers import LessonSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lesson(request, id: int):
    user = request.user
    serializer = LessonSerializer(services.read(id))
    return JsonResponse(serializer.data, safe=False)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def lessons(request, id=None):
    user = request.user

    if request.method == 'GET':
        serializer = LessonSerializer(services.read(id))
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':    # write
        data = json.loads(request.body)
        if not user.is_tutor:
            # TODO: refactor with permissions
            return JsonResponse({'message': 'Only for tutors!'}, status=403)
        serializer = LessonSerializer(data={**data, 'tutor': user.id})
        if serializer.is_valid():
            lesson = services.create(serializer)
            return JsonResponse(message.data, safe=False)
        else:
            return JsonResponse(serializer._errors, status=400)

    if request.method == 'PUT':     # edit
        pass
