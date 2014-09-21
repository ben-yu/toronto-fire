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
    start_datetime = models.DateTimeField(default=timezone.now)
    arrival_datetime = models.DateTimeField(default=timezone.now)
    end_datetime = models.DateTimeField(default=timezone.now)
    alarm_level = models.IntegerField(default=0)
    number_of_units = models.IntegerField(default=0)
    duration_in_min = models.IntegerField(default=0)

    @property
    def get_duration(self):
        """ 
        Returns the duration of the incident in seconds, which is
        the difference between end_datetime and start_datetime
        """
        if self.start_datetime and self.end_datetime:
            time_diff = self.end_datetime - self.start_datetime
            return time_diff.total_seconds()

    