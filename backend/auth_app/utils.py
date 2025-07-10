# Helper for supabase auth
# digest

import jwt
from django.conf import settings
from django.http import JsonResponse

def verify_supabase_jwt(token):
    try:
        payload = jwt.decode(
            token,
            settings.DB_JWT_SECRET,
            algorithms=["HS256"]
        )
        return payload
    except jwt.ExpiredSignatureError:
        return JsonResponse({'error': 'Token expired'}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({'error': 'Invalid token'}, status=401)
