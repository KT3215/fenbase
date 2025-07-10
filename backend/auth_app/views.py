# Supabase verification handling (JWT)
# Digest
import requests
import jwt
from django.http import JsonResponse
from .utils import verify_supabase_jwt

def whoami(request):
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return JsonResponse({'error': 'Missing or invalid Authorization header'}, status=401)

    token = auth_header.split(" ")[1]
    payload = verify_supabase_jwt(token)
    if isinstance(payload, JsonResponse):
        return payload  # error

    return JsonResponse({'user_id': payload['sub'], 'email': payload['email']})
