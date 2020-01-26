from django.http import JsonResponse
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

import json
from user.serializers import UserSerializer

from . import services

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        users = services.search(query, ~user.is_tutor)
        return JsonResponse(UserSerializer(users, many=True).data, safe=False)
    # return JsonResponse(list(map(lambda x: x.json_repr, users)), safe=False)

@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def single_user(request, user_id):

    if request.method == 'GET':
        user = services.get_user(id=user_id)
        return JsonResponse(user.json_repr)

    if request.method == 'PATCH':
        data = json.loads(request.body)
        for key in data.keys():
            if key not in {'name', 'surname', 'phone', 'address', 'photo'}:
                return JsonResponse({
                    'message': 'Only name, surname, phone, address and photo may be changed'},
                    status=400)
        # TODO: actually change values
        # TODO: save an object


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    if request.method == 'GET':
        user = request.user
        return JsonResponse(UserSerializer(user).data)
