from django.core.management.base import BaseCommand, CommandError
from toronto_fire.models import Incident
from datetime import datetime
import csv

class Command(BaseCommand):
    args = '<filename ...>'
    help = 'Import Incidents from a csv file'

    def handle(self, *args, **options):
        for filename in args:
            print filename
            with open(filename, 'rb') as csvfile:
                incident_reader = csv.reader(csvfile)
                next(incident_reader) # skip header row
                for incident_row in incident_reader:
                    if incident_row[6]:
                        incident_number = incident_row[6]
                        incident,created = Incident.objects.get_or_create(incident_number=incident_number)
                        incident.incident_type = incident_row[7] if incident_row[7] else "No Type"
                        incident.alarm_level = incident_row[8] if incident_row[8] else 0
                        # Responding units is a comma-delimited string of units numbers
                        # We'll count the units listed
                        incident.number_of_units = len(filter(None, incident_row[10].split(','))) if ',' in incident_row[10] else 0

                        incident.start_datetime = datetime.strptime(incident_row[5],'%Y-%m-%d   %I:%M:%S %p')
                        incident.arrival_datetime = datetime.strptime(incident_row[11],'%Y-%m-%d   %I:%M:%S %p')
                        incident.end_datetime = datetime.strptime(incident_row[12],'%Y-%m-%d   %I:%M:%S %p')

                        incident.save()