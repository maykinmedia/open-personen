from django.test import TestCase

from openpersonen.features import get_gebruik_in_lopende_tekst


aanduiding_naamgebruik_to_enumeration = {
    "Eigen": "E",
    "Partner na eigen": "N",
    "Partner": "P",
    "Partner voor eigen": "V",
}

geslachtsaanduiding_to_enumeration = {"Man": "M", "Vrouw": "V"}


class TestGetGebruikInLopendeTekstWithPrefix(TestCase):
    def test_gebruik_in_lopende_tekst_with_prefix(self):
        table_string = """
            | aanduidingNaamgebruik | geslachtsaanduiding |samenstelling gebruikInLopendeTekst | aanschrijfwijze           | gebruikInLopendeTekst          |
            | Eigen                 | Man                 | GA VV GN                           | H. in het Veld            | de heer In het Veld            |
            | Eigen                 | Man                 | GA VV GN                           | F. Groenen                | de heer Groenen                |
            | Partner na eigen      | Vrouw               | GA VV GN-VP GP                     | I. van Velzen-in het Veld | mevrouw Van Velzen-in het Veld |
            | Partner na eigen      | Vrouw               | GA VV GN-VP GP                     | F. Groenen-Groenink       | mevrouw Groenen-Groenink       |
            | Partner               | Vrouw               | GA VP GP                           | S. van Velzen             | mevrouw Van Velzen             |
            | Partner               | Vrouw               | GA VP GP                           | J.F.R. Groenen            | mevrouw Groenen                |
            | Partner voor eigen    | Man                 | GA VP GP-VV GN                     | F. in het Veld-van Velzen | de heer In het Veld-van Velzen |
            | Partner voor eigen    | Man                 | GA VP GP-VV GN                     | F. Groenen-Groenink       | de heer Groenen-Groenink       |
                """

        # Convert table string to rows and remove empty rows, white spaces, and header row
        table_rows = [
                         [item.strip() for item in row.strip().split("|") if item]
                         for row in table_string.split("\n")
                         if row.strip()
                     ][1:]

        for row in table_rows:
            (
                aanduiding_naamgebruik,
                gender,
                _,
                aanschrijfwijze,
                gebruik_in_lopende_tekst
            ) = row

            last_name = None
            last_name_prefix = None
            partner_last_name_prefix = None
            partner_last_name = None

            if aanduiding_naamgebruik == "Eigen":
                last_name = aanschrijfwijze.split(" ", 1)[-1]
                if len(last_name.split(" ")) > 1:
                    split_last_name = last_name.split(" ")
                    last_name_prefix = " ".join(split_last_name[:-1])
                    last_name = split_last_name[-1]
            elif aanduiding_naamgebruik == "Partner na eigen":
                last_name = aanschrijfwijze.split(" ", 1)[-1]
                last_name, partner_last_name = last_name.split("-")
                if len(last_name.split(" ")) > 1:
                    split_last_name = last_name.split(" ")
                    last_name_prefix = " ".join(split_last_name[:-1])
                    last_name = split_last_name[-1]
                if len(partner_last_name.split(" ")) > 1:
                    split_partner_last_name = partner_last_name.split(" ")
                    partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                    partner_last_name = split_partner_last_name[-1]
            elif aanduiding_naamgebruik == "Partner":
                partner_last_name = aanschrijfwijze.split(" ", 1)[-1]
                if len(partner_last_name.split(" ")) > 1:
                    split_partner_last_name = partner_last_name.split(" ")
                    partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                    partner_last_name = split_partner_last_name[-1]
            elif aanduiding_naamgebruik == "Partner voor eigen":
                last_name = aanschrijfwijze.split(" ", 1)[-1]
                partner_last_name, last_name = last_name.split("-")
                if len(last_name.split(" ")) > 1:
                    split_last_name = last_name.split(" ")
                    last_name_prefix = " ".join(split_last_name[:-1])
                    last_name = split_last_name[-1]
                if len(partner_last_name.split(" ")) > 1:
                    split_partner_last_name = partner_last_name.split(" ")
                    partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                    partner_last_name = split_partner_last_name[-1]

            with self.subTest(aanschrijfwijze=aanschrijfwijze):
                result = get_gebruik_in_lopende_tekst(
                    last_name_prefix,
                    last_name,
                    partner_last_name_prefix,
                    partner_last_name,
                    aanduiding_naamgebruik_to_enumeration[aanduiding_naamgebruik],
                    geslachtsaanduiding_to_enumeration[gender],
                    None,
                    None,
                )

                self.assertEqual(gebruik_in_lopende_tekst, result)
