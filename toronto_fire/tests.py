from django.test import TestCase
from toronto_fire.models import Incident
from django.db.models import Avg
from datetime import datetime
from django.core import management
import os

class IncidentTestCase(TestCase):
    def setUp(self):
        Incident.objects.create(incident_number='F10150021',start_datetime=datetime.strptime('2011-01-01  12:02:50 AM','%Y-%m-%d   %I:%M:%S %p'), \
            arrival_datetime=datetime.strptime('2011-01-01  12:12:06 AM','%Y-%m-%d   %I:%M:%S %p'), \
            end_datetime=datetime.strptime('2011-01-01  12:12:00 AM','%Y-%m-%d   %I:%M:%S %p'), \
            number_of_units=1, incident_type='Type 1 - thing', duration_in_min=10.0 )
        Incident.objects.create(incident_number='F10150022',start_datetime=datetime.strptime('2011-01-01  12:02:50 AM','%Y-%m-%d   %I:%M:%S %p'), \
            arrival_datetime=datetime.strptime('2011-01-01  12:12:06 AM','%Y-%m-%d   %I:%M:%S %p'), \
            end_datetime=datetime.strptime('2011-01-01  12:35:00 AM','%Y-%m-%d   %I:%M:%S %p'), \
            number_of_units=3, incident_type='Type 1 - stuff',duration_in_min=33.0)


    def test_incident_creation(self):
        """ Incidents are being properly created """
        incident = Incident.objects.get(incident_number="F10150021")

        self.assertEqual(incident.incident_number,"F10150021")
    
    def test_avg_units_by_type(self):
        """ Test avg_units_by_type() in IncidentQuerySet"""
        avg_num_of_trucks =  Incident.objects.avg_units_by_type()

        self.assertEqual(list(avg_num_of_trucks)[0]['number_of_units'],2.0)

    def test_avg_units_and_duration_by_level(self):
        """ Test avg_units_by_type() in IncidentQuerySet"""
        avg_num_of_trucks =  Incident.objects.avg_units_and_duration_by_level()

        self.assertEqual(list(avg_num_of_trucks)[0]['number_of_units'],2.0)
        self.assertEqual(list(avg_num_of_trucks)[0]['avg_duration'],21.5)

class ImportIncidentTestCase(TestCase):
    def setUp(self):
        # Create a csv file with a single row
        import csv
        header_row = ['PrimeStreet','CrossStreet','LookupIntersection','Latitude','Longitude','DispatchTime','IncidentNo','IncidentType','AlarmLevel','Area','DispatchedUnits','IncidentLoadTime','MAX(FireDispatchUpdate)']
        test_row = ['MOUNT PLEASANT RD', 'TT   LAWRENCE AVE E / WANLESS AVE','MOUNT PLEASANT RD and LAWRENCE AVE E Toronto','43.7261546','-79.3971892','2011-01-01  00:07:23',\
        'F11000011','Carbon Monoxide - Non Medical','1','131','A131,','2011-01-01  00:07:23','2011-01-01  00:10:33']

        test_csv = open('unittest.csv', 'wb')
        wr = csv.writer(test_csv, quoting=csv.QUOTE_ALL)
        wr.writerow(header_row)
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
        self.assertEqual(incident.alarm_level,1)
        self.assertEqual(incident.number_of_units,1)
        self.assertEqual(incident.duration_in_min,3)
