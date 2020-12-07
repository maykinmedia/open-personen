import csv

from django.core.management import BaseCommand, CommandError

import requests

from openpersonen.features.country_code_and_omschrijving.models import (
    CountryCodeAndOmschrijving,
)


class Command(BaseCommand):
    """
    Run using
    python src/manage.py import_country_codes_and_omschrijving --url='https://url.com/file.csv'
    or
    python src/manage.py import_country_codes_and_omschrijving --file=/path/To/file.csv
    """

    help = "Read in a csv file from a url or file path and populate models"

    def add_arguments(self, parser):
        parser.add_argument("--url", help="Url to csv file")
        parser.add_argument(
            "--file", help="The csv file containing the data to import."
        )

    def handle(self, **options):

        if options.get("url") and options.get("file"):
            raise CommandError("Please specify a url or file, not both")
        if not options.get("url") and not options.get("file"):
            raise CommandError("Must give a url or file")

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
            raise CommandError("Landcode should be the first column in your csv")
        if "Omschrijving" not in header_row[1]:
            raise CommandError("Omschrijving should be the second column in your csv")

        countries = [
            CountryCodeAndOmschrijving(code=row[0], omschrijving=row[1]) for row in rows
        ]

        CountryCodeAndOmschrijving.objects.bulk_create(countries)

        self.stdout.write(f"Done! {len(countries)} imported!")
