import csv

import requests

from django.core.management import BaseCommand


class Command(BaseCommand):
    """
    Run using python src/manage import_demodata --url=https://www.example.com/file.csv
    or using docker
    docker-compose run web python src/manage.py import_demodata --url=https://www.example.com/file.csv
    """

    help = "Read in an ods file from a url and populate models to use for demo data"

    def add_arguments(self, parser):
        parser.add_argument("--url", help="Url to csv file")
        parser.add_argument(
            "--file", help="The csv file containing the data to import."
        )

    def handle(self, **options):

        if options.get("url") and options.get("file"):
            self.stderr.write("Please specify a url or file, not both")
            return exit(1)
        if not options.get("url") and not options.get("file"):
            self.stderr.write("Must give a url or file")
            return exit(1)

        self.stdout.write("Importing country codes")

        if options.get("url"):
            with requests.Session() as s:
                download = s.get(options["url"])

                decoded_content = download.content.decode('utf-16')

                cr = csv.reader(decoded_content.splitlines(), delimiter=',')
                my_list = list(cr)
                for row in my_list:
                    print(row)
        else:
            with open(options["file"], 'r', newline='\n', encoding='utf-16') as csvfile:
                rows = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in rows:
                    print(', '.join(row))

        self.stdout.write("Done!")
