# Api endpoint to fetch announcements table

import os
from django.http import JsonResponse
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()  

SUPABASE_URL = os.getenv("DB_URL")
SUPABASE_KEY = os.getenv("DB_SERVICE_ROLE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_announcements(request):
    try:
        data = supabase.table("announcements").select("*").order("created_at", desc=True).execute()
        return JsonResponse({'announcements': data.data})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
