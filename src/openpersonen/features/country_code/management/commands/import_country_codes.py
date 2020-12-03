import csv

from django.core.management import BaseCommand

import requests

from openpersonen.features.country_code.models import CountryCode


class Command(BaseCommand):
    """
    Run using
    python src/manage.py import_country_codes --url='https://url.com/file.csv'
    or
    python src/manage.py import_country_codes --file=/path/To/file.csv
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
                decoded_content = download.content.decode("utf-16")
                rows = list(csv.reader(decoded_content.splitlines(), delimiter=","))
        else:
            with open(options["file"], "r", newline="\n", encoding="utf-16") as csvfile:
                rows = list(csv.reader(csvfile, delimiter=",", quotechar='"'))

        header_row = rows.pop(0)

        if "Landcode" not in header_row[0]:
            self.stderr.write("Landcode should be the first column in your csv")
            return exit(1)
        if "Omschrijving" not in header_row[1]:
            self.stderr.write("Omschrijving should be the first column in your csv")
            return exit(1)

        num_rows = 0
        for row in rows:
            CountryCode.objects.create(code=row[0], omschrijving=row[1])
            num_rows += 1

        self.stdout.write(f"Done! {num_rows} imported!")
