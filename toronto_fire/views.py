from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from django.db.models import Avg
import json

from toronto_fire.models import Incident

class IncidentsView(View):

    def get(self, request, *args, **kwargs):
        avg_num_of_trucks = Incident.objects.avg_units_by_type()
        avg_trucks_and_duration = Incident.objects.values('alarm_level').annotate(number_of_units = Avg('number_of_units'),\
            avg_duration = Avg('duration_in_min')).values('alarm_level','number_of_units','avg_duration') 
        context = {'avg_num_of_trucks': json.dumps(list(avg_num_of_trucks)),'avg_trucks_and_duration':json.dumps(list(avg_trucks_and_duration))}
        return render(request, 'incidents.html', context)