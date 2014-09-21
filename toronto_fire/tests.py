from django.test import TestCase
from toronto_fire.models import Incident
from django.db.models import Avg
from datetime import datetime

class IncidentTestCase(TestCase):
    def setUp(self):
        Incident.objects.create(incident_number='F10150021',start_datetime=datetime.strptime('2011-01-01  12:02:50 AM','%Y-%m-%d   %I:%M:%S %p'), \
            arrival_datetime=datetime.strptime('2011-01-01  12:12:06 AM','%Y-%m-%d   %I:%M:%S %p'), end_datetime=datetime.strptime('2011-01-01  12:35:00 AM','%Y-%m-%d   %I:%M:%S %p'))

    def test_incident_creation(self):
        """ Incidents are being properly created """
        incident = Incident.objects.get(incident_number="F10150021")

        self.assertEqual(incident.incident_number,"F10150021")
