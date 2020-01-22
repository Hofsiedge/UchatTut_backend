# api_auth/views.py
from django.contrib.auth import authenticate, get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
        HTTP_400_BAD_REQUEST,
        HTTP_404_NOT_FOUND,
        HTTP_200_OK
)
from rest_framework.response import Response
import json

from user.serializers import UserSerializer


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    if email is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=email, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

@api_view(['POST'])
@permission_classes((AllowAny, ))
def register(request):
    VALID_USER_FIELDS = [f.name for f in get_user_model()._meta.fields]
    serializer = UserSerializer(data=json.loads(request.body))
    if serializer.is_valid():
        user_data = {field: data for (field, data) in request.data.items() 
                     if field in VALID_USER_FIELDS}
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        # return Response(serializer.data, status=201)
        return Response({"token": token}, status=201)
    return Response(serializer._errors, status=400)

