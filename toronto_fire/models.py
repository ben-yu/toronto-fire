from django.db import models
from django.utils import timezone

class Incident(models.Model):
    """
    Any incident in the toronto-fire dataset are represented
    by this model.

    Incidents are identified by incident_number, and must have
    a start, arrival and end time
    """
    incident_number = models.CharField(max_length=30, unique=True)
    incident_type = models.CharField(max_length=255, default="No Type")
    start_datetime = models.DateField(default=timezone.now)
    arrival_datetime = models.DateField(default=timezone.now)
    end_datetime = models.DateField(default=timezone.now)
    alarm_level = models.IntegerField(default=0)
    number_of_units = models.IntegerField(default=0)

    