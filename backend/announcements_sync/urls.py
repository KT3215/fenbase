from django.urls import path
from .views import get_announcements

urlpatterns = [
    path("all/", get_announcements),
]
