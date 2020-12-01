from django.test import TestCase

from openpersonen.features import get_gebruik_in_lopende_tekst
from openpersonen.features.constants import *

aanduiding_naamgebruik_to_enumeration = {
    "Eigen": EIGEN,
    "Partner na eigen": PARTNER_NA_EIGEN,
    "Partner": PARTNER,
    "Partner voor eigen": PARTNER_VOOR_EIGEN,
}

geslachtsaanduiding_to_enumeration = {
    "Man": MALE,
    "Vrouw": FEMALE,
    "man": MALE,
    "vrouw": FEMALE,
}


class TestGetGebruikInLopendeTekstWithoutTitleOrPredicate(TestCase):
    def test_gebruik_in_lopende_tekst_without_title_or_predicate(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/gebruik_in_lopende_tekst.feature#L73-L82
        """
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
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/gebruik_in_lopende_tekst.feature#L84-L89
        """
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
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/gebruik_in_lopende_tekst.feature#L91-L99
        """
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
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/gebruik_in_lopende_tekst.feature#L101-L109
        """
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

            gender = None
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


class TestGetGebruikInLopendeTekstPartnerTitleOrPredikaat(TestCase):
    def test_gebruik_in_lopende_tekst_partner_title_or_predikaat(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/gebruik_in_lopende_tekst.feature#L111-L127
        """
        table_string = """
            | geslachtsaanduiding | geslachtsaanduiding partner | adellijkeTitel_predikaat partner | aanduidingNaamgebruik | aanschrijfwijze                         | gebruikInLopendeTekst                      |
            | V                   | M                           | Baron                            | Eigen                 | A.C. van der Veen                       | mevrouw Van der Veen                       |
            | V                   | M                           | Baron                            | Partner na eigen      | A.C. van der Veen-barones van den Aedel | mevrouw Van der Veen-barones van den Aedel |
            | V                   | M                           | Baron                            | Partner               | A.C. barones van den Aedel              | barones Van den Aedel                      |
            | V                   | M                           | Baron                            | Partner voor eigen    | A.C. barones van den Aedel-van der Veen | barones Van den Aedel-van der Veen         |
            | M                   | V                           | Gravin                           | Eigen                 | W. van der Veen                         | de heer Van der Veen                       |
            | M                   | V                           | Gravin                           | Partner na eigen      | W. van der Veen-graaf van den Aedel     | de heer Van der Veen-van den Aedel         |
            | M                   | V                           | Gravin                           | Partner               | W. graaf van den Aedel                  | de heer Van den Aedel                      |
            | M                   | V                           | Gravin                           | Partner voor eigen    | W. graaf van den Aedel-van der Veen     | de heer Van den Aedel-van der Veen         |
            | M                   | M                           | Baron                            | Partner na eigen      | W. van der Veen-van den Aedel           | de heer Van der Veen-van den Aedel         |
            | V                   | V                           | Barones                          | Partner na eigen      | W. van der Veen-van den Aedel           | mevrouw Van der Veen-van den Aedel         |
            | V                   | M                           | Ridder                           | Partner na eigen      | W. van der Veen-van den Aedel           | mevrouw Van der Veen-van den Aedel         |
            | V                   | M                           | Jonkheer                         | Eigen                 | A.C. van der Veen                       | mevrouw Van der Veen                       |
            | V                   | M                           | Jonkheer                         | Partner na eigen      | A.C. van der Veen-van den Aedel         | mevrouw Van der Veen-van den Aedel         |
            | V                   | M                           | Jonkheer                         | Partner               | A.C. van den Aedel                      | mevrouw Van den Aedel                      |
            | V                   | M                           | Jonkheer                         | Partner voor eigen    | A.C. van den Aedel-van der Veen         | mevrouw Van den Aedel-van der Veen         |
        """

        # Convert table string to rows and remove empty rows, white spaces, and header row
        table_rows = [
            [item.strip() for item in row.strip().split("|") if item]
            for row in table_string.split("\n")
            if row.strip()
        ][1:]

        for row in table_rows:
            (
                gender,
                partner_gender,
                partner_title,
                aanduiding_naamgebruik,
                aanschrijfwijze,
                gebruik_in_lopende_tekst,
            ) = row

            last_name = gebruik_in_lopende_tekst
            for salutation in [
                "mevrouw ",
                "barones ",
                "de heer ",
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

            with self.subTest(
                gender=gender,
                partner_gender=partner_gender,
                partner_title=partner_title,
                aanduiding_naamgebruik=aanduiding_naamgebruik,
            ):
                result = get_gebruik_in_lopende_tekst(
                    last_name_prefix,
                    last_name,
                    partner_last_name_prefix,
                    partner_last_name,
                    aanduiding_naamgebruik_to_enumeration[aanduiding_naamgebruik],
                    gender,
                    None,
                    partner_title,
                )

                self.assertEqual(gebruik_in_lopende_tekst, result)
