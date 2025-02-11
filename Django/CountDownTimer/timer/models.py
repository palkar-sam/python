from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    event_date = models.DateTimeField(timezone.now)

    def __str__(self):
        return self.name