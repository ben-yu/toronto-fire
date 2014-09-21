from django.test import TestCase
from toronto_fire.models import Incident
from django.db.models import Avg
from datetime import datetime
from django.core import management
import os

class IncidentTestCase(TestCase):
    def setUp(self):
        Incident.objects.create(incident_number='F10150021',start_datetime=datetime.strptime('2011-01-01  12:02:50 AM','%Y-%m-%d   %I:%M:%S %p'), \
            arrival_datetime=datetime.strptime('2011-01-01  12:12:06 AM','%Y-%m-%d   %I:%M:%S %p'), end_datetime=datetime.strptime('2011-01-01  12:35:00 AM','%Y-%m-%d   %I:%M:%S %p'))

    def test_incident_creation(self):
        """ Incidents are being properly created """
        incident = Incident.objects.get(incident_number="F10150021")

        self.assertEqual(incident.incident_number,"F10150021")

class ImportIncidentTestCase(TestCase):
    def setUp(self):
        # Create a csv file with a single row
        import csv
        test_row = ['MOUNT PLEASANT RD and LAWRENCE AVE E Toronto ','43.7261546','-79.3971892','2011-01-01  12:07:23 AM',\
        'F11000011','Carbon Monoxide - Non Medical','1','131','A131','2011-01-01  12:07:23 AM','2011-01-01  12:07:23 AM']

        test_csv = open('unittest.csv', 'wb')
        wr = csv.writer(test_csv, quoting=csv.QUOTE_ALL)
        wr.writerow(test_row)

    def tearDown(self):
        # Clean up test csv
        os.remove('unittest.csv')                     

    def test_import_incidents(self):
        """ 
        import_incidents command properly parses and create/updates
        incidents in the database from a csv file
        """

        management.call_command('import_incidents','unittest.csv')
        incident = Incident.objects.get(incident_number="F11000011")

        self.assertEqual(incident.incident_number,"F11000011")
