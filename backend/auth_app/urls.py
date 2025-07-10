#wip

from django.urls import path
from .views import whoami

urlpatterns = [
    path("whoami/", whoami),
]
