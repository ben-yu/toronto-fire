from django.db import models
from django.db.models.query import QuerySet
from django.db.models import Avg

class IncidentQuerySet(QuerySet):
    def avg_units_by_type(self):
        return self.values('incident_type').annotate(number_of_units = Avg('number_of_units'))\
        .values('incident_type','number_of_units').order_by('-number_of_units')

class IncidentManager(models.Manager):
    def get_queryset(self):
        return IncidentQuerySet(self.model)
    def __getattr__(self, attr, *args):
        # see https://code.djangoproject.com/ticket/15062 for details
        if attr.startswith("_"):
            raise AttributeError
        return getattr(self.get_queryset(), attr, *args)