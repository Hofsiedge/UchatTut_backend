from django.http import JsonResponse
import json
from .models import User

def user_list(request):
    if request.method == 'GET':
        data  = json.loads(request.body)
        users = User.objects
        users = users.filter(surname__startswith=data.get('surname', ''))
        users = users.filter(name__startswith=data.get('name', ''))
    return JsonResponse(list(map(lambda x: x.json_repr, users)), safe=False)

def single_user(request, user_id):
    if request.method == 'GET':
        user = User.objects.get(id=user_id)
        return JsonResponse(user.json_repr)
    if request.method == 'PATCH':
        data = json.loads(request.content)
        for key in data.keys():
            if key not in {'name', 'surname', 'phone', 'address', 'photo'}:
                return JsonResponse({
                    'message': 'Only name, surname, phone, address and photo may be changed'},
                    status=400)
        # TODO: actually change values
        # TODO: save an object

