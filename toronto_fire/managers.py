from django.db import models
from django.db.models.query import QuerySet
from django.db.models import Avg

class IncidentQuerySet(QuerySet):
    def avg_units_by_type(self):
        """ Average number of trucks by incident type """
        return self.values('incident_type').annotate(number_of_units = Avg('number_of_units'))\
        .values('incident_type','number_of_units').order_by('-number_of_units')

    def avg_units_and_duration_by_level(self):
        """ Average number of trucks and incident duration by incident level """
        return self.values('alarm_level').annotate(number_of_units = Avg('number_of_units'),\
            avg_duration = Avg('duration_in_min')).values('alarm_level','number_of_units','avg_duration') 

    def avg_values_by_types(self,*args,**kwargs):
        """ Builds a query that calculates averages """
        raise NotImplementedError       

class IncidentManager(models.Manager):
    def get_queryset(self):
        return IncidentQuerySet(self.model)
    def __getattr__(self, attr, *args):
        # see https://code.djangoproject.com/ticket/15062 for details
        if attr.startswith("_"):
            raise AttributeError
        return getattr(self.get_queryset(), attr, *args)