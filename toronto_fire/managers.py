from django.db import models
from django.db.models.query import QuerySet
from django.db.models import Avg
from itertools import groupby

class IncidentQuerySet(QuerySet):
    def avg_units_by_type(self):
        """ Average number of trucks by incident type """
        def get_parent_type(incident_obj):
            """ returns the parent type that appears before a hyphen """
            incident_obj['incident_type'] = incident_obj['incident_type'].split('-')[0].strip()
            return incident_obj

        def reduce_count(x,y):
            incident_obj = x
            incident_obj['number_of_units'] = x['number_of_units'] + y['number_of_units']
            return incident_obj

        avg_units = self.values('incident_type').annotate(number_of_units = Avg('number_of_units'))\
        .values('incident_type','number_of_units')
        # convert queryset to a list
        avg_units = list(avg_units)
        # map all incident types to the substring before a hyphen
        avg_units = map(get_parent_type, avg_units)

        # groupby incident type
        groups = []
        data = sorted(avg_units, key=lambda x: x['incident_type'])
        for k, g in groupby(data, lambda x: x['incident_type']):
            groups.append(list(g))
        result = []

        # calculate the average for each group
        for group in groups:
            if len(group) < 2: 
                result.append(group[0])
                continue
            type_count = reduce(reduce_count,group)
            print type_count
            result.append({'incident_type':group[0]['incident_type'],'number_of_units':type_count['number_of_units']/len(group)})

        # Sort the resulting array by number of trucks
        result = sorted(result, key=lambda x: x['number_of_units'])
        return result

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