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
import requests
from rest_framework.response import Response
import json

from uchattut.settings import FB_APP_KEY
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

    fcm_token = request.data.get("fcm_token")
    if validate_fmc_token(fcm_token):
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                        status=HTTP_200_OK)

    return Response({'error': 'Invalid FCM_Token'},
                    status=HTTP_404_NOT_FOUND)




@api_view(['POST'])
@permission_classes((AllowAny,))
def register(request):
    serializer = UserSerializer(data=json.loads(request.body))
    if serializer.is_valid():
        fcm_token = request.data.get("fcm_token")
        if validate_fmc_token(fcm_token):
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=201)

        return Response({'error': 'Invalid FCM_Token'},
                        status=HTTP_404_NOT_FOUND)

    return Response(serializer._errors, status=400)


def validate_fmc_token(token):
    if token is None:
        # return {'error': 'Please provide FCM_Token'}
        return False

    payload = {'registration_ids': [token], 'dry_run': True}
    headers = {'Content-Type': 'application/json', 'Authorization': 'key=' + FB_APP_KEY}
    r = requests.post('https://fcm.googleapis.com/fcm/send', data=json.dumps(payload), headers=headers)
    if r.status_code != 200:
        # return {'error': 'Invalid FB_APP_KEY'}
        return False
    r = r.json()
    if not r['success'] == 1:
        # return {'error': 'Invalid FCM_Token'}
        return False
    return True
