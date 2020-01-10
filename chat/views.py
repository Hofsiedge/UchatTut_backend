# from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def chat_list(request):
    return JsonResponse([
        {"id": 1, "name": "", "users": [0, 1]},
        {"id": 2, "name": "", "users": [0, 2]},
        {"id": 3, "name": "Chat #", "users": [0, 1, 2]},
    ], safe=False) # safe=True only allows to send dicts

# depth states for how many message batches to load (30 for each level)
def chat(request, chat_id, depth=1): 
    return JsonResponse([], safe=False)
