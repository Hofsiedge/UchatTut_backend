# from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    return JsonResponse({'dialogues': [
        {"id": 1, "name": "Dilogue 1", 
         "last_message": {"sender": 123, "message": "The last message of this dialogue"}},
        {"id": 2, "name": "Dilogue 2",
         "last_message": {"sender": 124, "message": "Almost the last message of this dialogue"}},
        {"id": 3, "name": "Dilogue 3",
         "last_message": {"sender": 125, "message": "Definitely the last message of this dialogue"}},
    ]})

# depth states for how many message batches to load (30 for each level)
def chat(request, chat_id, depth=1): 
    return JsonResponse({"messages": []})
