from django.test import TestCase

from openpersonen.features.aanschrijfwijze import get_aanschrijfwijze


class TestGetAanschrijfwijzeWithPrefix(TestCase):
    def test_aanschrijfwijze_with_prefix(self):
        table_string = """
            | aanduidingAanschrijving | samenstelling aanschrijfwijze | voorvoegsel | geslachtsnaam | voornamen | voorvoegsel partner | geslachtsnaam partner | aanschrijfwijze           |
            | E                       | VL VV GN                      | In het      | Veld          | Henk      | van                 | Velzen                | H. In het Veld            |
            | N                       | VL VV GN-VP GP                | van         | Velzen        | Ingrid    | In het              | Veld                  | I. van Velzen-In het Veld |
            | P                       | VL VP GP                      | In het      | Veld          | Suzanne   | van                 | Velzen                | S. van Velzen             |
            | V                       | VL VP GP-VV GN                | van         | Velzen        | Fred      | In het              | Veld                  | F. In het Veld-van Velzen |
        """

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


class TestGetAanschrijfwijzeWithoutPrefix(TestCase):
    def test_aanschrijfwijze_without_prefix(self):
        table_string = """
            | aanduidingAanschrijving | samenstelling aanschrijfwijze | geslachtsnaam | voornamen          | aanschrijfwijze     |
            | E                       | VL GN                         | Groenen       | Franklin           | F. Groenen          |
            | N                       | VL GN-GP                      | Groenen       | Franka             | F. Groenen-Groenink |
            | P                       | VL GP                         | Groenink      | Johan Frank Robert | J.F.R. Groenen      |
            | V                       | VL GP-GN                      | Groenlo       | Franka             | F. Groenen-Groenlo  |
        """

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
                geslachtsnaam,
                voornamen,
                aanschrijfwijze,
            ) = row

            geslachtsnaam_partner = None
            if aanduiding_aanschrijving == "N":
                last_name = aanschrijfwijze.split(" ", 1)[-1]
                _, geslachtsnaam_partner = last_name.split("-")
            elif aanduiding_aanschrijving == "P":
                geslachtsnaam_partner = aanschrijfwijze.split(" ", 1)[-1]
            elif aanduiding_aanschrijving == "V":
                last_name = aanschrijfwijze.split(" ", 1)[-1]
                geslachtsnaam_partner, _ = last_name.split("-")

            result = get_aanschrijfwijze(
                None,
                geslachtsnaam,
                voornamen,
                None,
                geslachtsnaam_partner,
                aanduiding_aanschrijving,
                None,
                None,
                None,
            )

            self.assertEqual(aanschrijfwijze, result)
