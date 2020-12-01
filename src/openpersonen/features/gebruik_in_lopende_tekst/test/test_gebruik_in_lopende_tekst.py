from django.test import TestCase

from openpersonen.features import get_gebruik_in_lopende_tekst
from openpersonen.features.constants import *


aanduiding_naamgebruik_to_enumeration = {
    "Eigen": "E",
    "Partner na eigen": "N",
    "Partner": "P",
    "Partner voor eigen": "V",
}

geslachtsaanduiding_to_enumeration = {
    "Man": "M",
    "Vrouw": "V",
    "man": "M",
    "vrouw": "V",
}


class TestGetGebruikInLopendeTekstWithoutTitleOrPredicate(TestCase):
    def test_gebruik_in_lopende_tekst_without_title_or_predicate(self):
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
                gebruik_in_lopende_tekst,
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


class TestGetGebruikInLopendeTekstVoervoegselsWithSmallOrCapitalLetters(TestCase):
    def test_gebruik_in_lopende_tekst_without_title_or_predicate(self):
        table_string = """
            | aanduidingAanschrijving | geslachtsaanduiding | VV     | GN     | VP     | GP     | gebruikInLopendeTekst          |
            | E                       | man                 | In het | Veld   | van    | Velzen | de heer In het Veld            |
            | N                       | vrouw               | van    | Velzen | In het | Veld   | mevrouw Van Velzen-In het Veld |
            | P                       | vrouw               | In het | Veld   | van    | Velzen | mevrouw Van Velzen             |
            | V                       | man                 | van    | Velzen | In het | Veld   | de heer In het Veld-van Velzen |
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
                gender,
                last_name_prefix,
                last_name,
                partner_last_name_prefix,
                partner_last_name,
                gebruik_in_lopende_tekst,
            ) = row

            with self.subTest(aanduiding_aanschrijving=aanduiding_aanschrijving):
                result = get_gebruik_in_lopende_tekst(
                    last_name_prefix,
                    last_name,
                    partner_last_name_prefix,
                    partner_last_name,
                    aanduiding_aanschrijving,
                    geslachtsaanduiding_to_enumeration[gender],
                    None,
                    None,
                )

                self.assertEqual(gebruik_in_lopende_tekst, result)


class TestGetGebruikInLopendeTekstWithAdelijkeTitel(TestCase):
    def test_gebruik_in_lopende_tekst_with_adelijke_title(self):
        table_string = """
            | adellijkeTitel_predikaat | aanduidingNaamgebruik | geslachtsaanduiding | samenstelling gebruikInLopendeTekst | gebruikInLopendeTekst                        |
            | Baron                    | Eigen                 | Man                 | AT VV GN                            | baron Van den Aedel                          |
            | Barones                  | Partner na eigen      | Vrouw               | AT VV GN-VP GP                      | barones Van den Aedel-van der Veen           |
            | Graaf                    | Partner               | Man                 | GA VP GP                            | de heer Van der Veen                         |
            | Gravin                   | Partner voor eigen    | Vrouw               | GA VP GP-AT VV GN                   | mevrouw Van der Veen-gravin van den Aedel    |
            | Prins                    | Eigen                 | Man                 | AT VV GN                            | prins Van Roodt de Wit Blaauw                |
            | Prinses                  | Eigen                 | Vrouw               | AT VV GN                            | prinses Van Roodt de Wit Blaauw              |
            | Ridder                   | Eigen                 | Man                 | T VV GN                             | ridder Van Hoogh                             |
        """

        # Convert table string to rows and remove empty rows, white spaces, and header row
        table_rows = [
            [item.strip() for item in row.strip().split("|") if item]
            for row in table_string.split("\n")
            if row.strip()
        ][1:]

        for row in table_rows:
            (
                title,
                aanduiding_naamgebruik,
                gender,
                _,
                gebruik_in_lopende_tekst,
            ) = row

            last_name = gebruik_in_lopende_tekst
            for salutation in [
                "baron ",
                "barones ",
                "de heer ",
                "mevrouw ",
                "prins ",
                "prinses ",
                "ridder ",
            ]:
                last_name = last_name.replace(salutation, "")

            last_name_prefix = None
            partner_last_name_prefix = None
            partner_last_name = None

            if aanduiding_naamgebruik == "Eigen":
                if len(last_name.split(" ")) > 1:
                    split_last_name = last_name.split(" ")
                    last_name_prefix = " ".join(split_last_name[:-1])
                    last_name = split_last_name[-1]
            elif aanduiding_naamgebruik == "Partner na eigen":
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
                partner_last_name = last_name
                if len(partner_last_name.split(" ")) > 1:
                    split_partner_last_name = partner_last_name.split(" ")
                    partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                    partner_last_name = split_partner_last_name[-1]
            elif aanduiding_naamgebruik == "Partner voor eigen":
                partner_last_name, last_name = last_name.split("-")
                if len(last_name.split(" ")) > 1:
                    split_last_name = last_name.split(" ")
                    last_name_prefix = " ".join(split_last_name[:-1])
                    last_name = split_last_name[-1]
                if len(partner_last_name.split(" ")) > 1:
                    split_partner_last_name = partner_last_name.split(" ")
                    partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                    partner_last_name = split_partner_last_name[-1]

            with self.subTest(title=title):
                result = get_gebruik_in_lopende_tekst(
                    last_name_prefix,
                    last_name,
                    partner_last_name_prefix,
                    partner_last_name,
                    aanduiding_naamgebruik_to_enumeration[aanduiding_naamgebruik],
                    geslachtsaanduiding_to_enumeration[gender],
                    title,
                    None,
                )

                self.assertEqual(gebruik_in_lopende_tekst, result)


class TestGetGebruikInLopendeTekstWithPredikaat(TestCase):
    def test_gebruik_in_lopende_tekst_with_predikaat(self):
        table_string = """
            | adellijkeTitel_predikaat | aanduidingNaamgebruik | partner | aanhef                                  |
            | Jonkheer                 | Eigen                 | Geen    | jonkheer Van Hoogh                      |
            | Jonkvrouw                | Eigen                 | Geen    | jonkvrouw Van Hoogh                     |
            | Jonkheer                 | Eigen                 | Ja      | jonkheer Van Hoogh                      |
            | Jonkvrouw                | Eigen                 | Ja      | jonkvrouw Van Hoogh                     |
            | Jonkvrouw                | Partner na eigen      | Ja      | jonkvrouw Van Hoogh-in het Veld         |
            | Jonkvrouw                | Partner               | Ja      | mevrouw In het Veld                     |
            | Jonkvrouw                | Partner voor eigen    | Ja      | mevrouw In het Veld-jonkvrouw van Hoogh |
        """

        # Convert table string to rows and remove empty rows, white spaces, and header row
        table_rows = [
            [item.strip() for item in row.strip().split("|") if item]
            for row in table_string.split("\n")
            if row.strip()
        ][1:]

        for row in table_rows:
            (
                title,
                aanduiding_naamgebruik,
                has_partner,
                gebruik_in_lopende_tekst,
            ) = row

            last_name = gebruik_in_lopende_tekst
            for salutation in [
                "jonkheer ",
                "jonkvrouw ",
                "mevrouw ",
            ]:
                last_name = last_name.replace(salutation, "")

            if title == JONKHEER:
                gender = MALE
            elif title == JONKVROUW:
                gender = FEMALE

            last_name_prefix = None
            partner_last_name_prefix = None
            partner_last_name = None

            if aanduiding_naamgebruik == "Eigen":
                if len(last_name.split(" ")) > 1:
                    split_last_name = last_name.split(" ")
                    last_name_prefix = " ".join(split_last_name[:-1])
                    last_name = split_last_name[-1]
            elif aanduiding_naamgebruik == "Partner na eigen":
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
                partner_last_name = last_name
                if len(partner_last_name.split(" ")) > 1:
                    split_partner_last_name = partner_last_name.split(" ")
                    partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                    partner_last_name = split_partner_last_name[-1]
            elif aanduiding_naamgebruik == "Partner voor eigen":
                partner_last_name, last_name = last_name.split("-")
                if len(last_name.split(" ")) > 1:
                    split_last_name = last_name.split(" ")
                    last_name_prefix = " ".join(split_last_name[:-1])
                    last_name = split_last_name[-1]
                if len(partner_last_name.split(" ")) > 1:
                    split_partner_last_name = partner_last_name.split(" ")
                    partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                    partner_last_name = split_partner_last_name[-1]

            with self.subTest(
                title=title,
                aanduiding_naamgebruik=aanduiding_naamgebruik,
                has_partner=has_partner,
            ):
                result = get_gebruik_in_lopende_tekst(
                    last_name_prefix,
                    last_name,
                    partner_last_name_prefix,
                    partner_last_name,
                    aanduiding_naamgebruik_to_enumeration[aanduiding_naamgebruik],
                    gender,
                    title,
                    None,
                )

                self.assertEqual(gebruik_in_lopende_tekst, result)
