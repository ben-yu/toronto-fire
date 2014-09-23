from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from django.db.models import Avg
import json

from toronto_fire.models import Incident

class IncidentsView(View):

    def get(self, request, *args, **kwargs):
        avg_num_of_trucks = Incident.objects.avg_units_by_type()
        avg_trucks_and_duration = Incident.objects.avg_units_and_duration_by_level()
        context = {'avg_num_of_trucks': json.dumps(list(avg_num_of_trucks)),'avg_trucks_and_duration':json.dumps(list(avg_trucks_and_duration))}
        return render(request, 'incidents.html', context)