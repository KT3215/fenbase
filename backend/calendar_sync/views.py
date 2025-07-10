# handles oauth & manually syncs endpoints

from django.http import JsonResponse
from .tasks import simple, SimpleInput
from .tasks import simple

def get_events(request):
    result = simple.run(input=SimpleInput(message="Fetch calendar"))
    return JsonResponse({"status": "task started", "result": result})
