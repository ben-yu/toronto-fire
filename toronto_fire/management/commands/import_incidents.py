from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = '<filename ...>'
    help = 'Import Incidents from a csv file'

    def handle(self, *args, **options):
        raise NotImplementedError
        
                