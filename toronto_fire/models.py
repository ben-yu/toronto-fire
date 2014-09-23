from django.db import models
from django.utils import timezone

from toronto_fire.managers import IncidentManager

class Incident(models.Model):
    """
    Any incident in the toronto-fire dataset are represented
    by this model.

    Incidents are identified by incident_number, and must have
    a start, arrival and end time
    """
    incident_number = models.CharField(max_length=30, unique=True)
    incident_type = models.CharField(max_length=255, default="No Type")
    start_datetime = models.DateTimeField(default=timezone.now)
    arrival_datetime = models.DateTimeField(default=timezone.now)
    end_datetime = models.DateTimeField(default=timezone.now)
    alarm_level = models.IntegerField(default=0)
    number_of_units = models.IntegerField(default=0)
    duration_in_min = models.IntegerField(default=0)

    objects = IncidentManager() 
    