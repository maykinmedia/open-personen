from django.test import TestCase

from openpersonen.features.aanschrijfwijze import get_aanschrijfwijze


class TestGetAanschrijfwijzeWithoutTitle(TestCase):
    def test_aanschrijfwijze_without_title(self):
        table_string = """
            | aanduidingAanschrijving | samenstelling aanschrijfwijze | voorvoegsel | geslachtsnaam | voornamen | voorvoegsel partner | geslachtsnaam partner | aanschrijfwijze           |
            | E                       | VL VV GN                      | In het      | Veld          | Henk      | van                 | Velzen                | H. In het Veld            |
            | N                       | VL VV GN-VP GP                | van         | Velzen        | Ingrid    | In het              | Veld                  | I. van Velzen-In het Veld |
            | P                       | VL VP GP                      | In het      | Veld          | Suzanne   | van                 | Velzen                | S. van Velzen             |
            | V                       | VL VP GP-VV GN                | van         | Velzen        | Fred      | In het              | Veld                  | F. In het Veld-van Velzen |
        """

        aanduiding_naamgebruik_to_enumeration = {
            "Eigen": "E",
            "Partner na eigen": "N",
            "Partner": "P",
            "Partner voor eigen": "V",
        }

        geslachtsaanduiding_to_enumeration = {"Man": "M", "Vrouw": "V"}

        # Convert table string to rows and remove empty rows, white spaces, and header row
        table_rows = [
            [item.strip() for item in row.strip().split("|") if item]
            for row in table_string.split("\n")
            if row.strip()
        ][1:]

        for row in table_rows:
            (
                aanduiding_aanschrijving,
                _,
                voervoegsel,
                geslachtsnaam,
                voornamen,
                voervoegsel_partner,
                geslachtsnaam_partner,
                aanschrijfwijze,
            ) = row

            result = get_aanschrijfwijze(
                voervoegsel,
                geslachtsnaam,
                voornamen,
                voervoegsel_partner,
                geslachtsnaam_partner,
                aanduiding_aanschrijving,
                None,
                None,
                None,
            )

            self.assertEqual(aanschrijfwijze, result)
