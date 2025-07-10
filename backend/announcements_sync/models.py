# Fetch announcements
# Not testing this for now as I'm not sure if it's totally necessary
from django.db import models

class Announcement(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False  # Supabase manages this, Django reads only
        db_table = "announcements"
