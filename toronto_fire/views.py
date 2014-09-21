from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from django.db.models import Avg
import json

from toronto_fire.models import Incident

class IncidentsView(View):

    def get(self, request, *args, **kwargs):
        avg_num_of_trucks = Incident.objects.values('incident_type').annotate(number_of_units = Avg('number_of_units')).values('incident_type','number_of_units')
        context = {'avg_num_of_trucks': json.dumps(list(avg_num_of_trucks))}
        return render(request, 'incidents.html', context)