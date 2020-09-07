from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Read in an csv file and populate models to use for test data'

    def add_arguments(self, parser):
        parser.add_argument('infile', help='The csv file containing the data to import.')

    def handle(self, **options):
        print(f"Will import {options['infile']}")
