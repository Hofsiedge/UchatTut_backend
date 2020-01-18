from django.http import JsonResponse
from django.utils import timezone
import json
from .models import Message

def message(request):
    if request.method == 'POST':    # write
        data = json.loads(request.content)
        message = Message(text=data.get('text', ''),
                          # sender=request.
                         )
    if request.method == 'PUT':     # edit
        pass
