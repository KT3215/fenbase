# link and create urls for the calendar page
# URL should nav to Hatchet 

from django.urls import path
from .views import get_events

urlpatterns = [
    path("fetch/", get_events),
]