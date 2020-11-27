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


class TestGetAanschrijfwijzePersonHasTitlePartnerDoesNot(TestCase):
    def test_aanschrijfwijze_person_has_title_partner_does_not(self):
        table_string = """
            | aanduidingAanschrijving | samenstelling aanschrijfwijze | geslachtsnaam | voornamen      | aanschrijfwijze                        |
            | E                       | VL AT VV GN                   | Aedel         | Hendrik Willem | H.W. graaf van den Aedel               |
            | N                       | VL AT VV GN-VP GP             | Aedel         | Wilhelmina     | W. gravin van den Aedel-van der Veen   |
            | P                       | VL VP GP                      | Aedel         | Frederique     | F. van der Veen                        |
            | V                       | VL VP GP-AT VV GN             | Aedel         | Emma Louise    | E.L. van der Veen-gravin van den Aedel |
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

            last_name_prefix = None
            partner_last_name_prefix = None
            partner_last_name = None
            if aanduiding_aanschrijving == "E":
                last_name = aanschrijfwijze.split(" ", 1)[-1]
                split_last_name = last_name.split(" ")
                last_name_prefix = " ".join(split_last_name[:-1])
            elif aanduiding_aanschrijving == "N":
                last_name = aanschrijfwijze.split(" ", 1)[-1]
                last_name, partner_last_name = last_name.split("-")
                split_last_name = last_name.split(" ")
                last_name_prefix = " ".join(split_last_name[:-1])
                split_partner_last_name = partner_last_name.split(" ")
                partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                partner_last_name = split_partner_last_name[-1]
            elif aanduiding_aanschrijving == "P":
                partner_last_name = aanschrijfwijze.split(" ", 1)[-1]
                split_partner_last_name = partner_last_name.split(" ")
                partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                partner_last_name = split_partner_last_name[-1]
            elif aanduiding_aanschrijving == "V":
                last_name = aanschrijfwijze.split(" ", 1)[-1]
                partner_last_name, last_name = last_name.split("-")
                split_last_name = last_name.split(" ")
                last_name_prefix = " ".join(split_last_name[:-1])
                split_partner_last_name = partner_last_name.split(" ")
                partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                partner_last_name = split_partner_last_name[-1]

            result = get_aanschrijfwijze(
                last_name_prefix,
                geslachtsnaam,
                voornamen,
                partner_last_name_prefix,
                partner_last_name,
                aanduiding_aanschrijving,
                None,
                None,
                None,
            )

            self.assertEqual(aanschrijfwijze, result)


class TestGetAanschrijfwijzePersonHasPredicatePartnerDoesNot(TestCase):
    def test_aanschrijfwijze_person_has_predicate_partner_does_not(self):
        table_string = """
            | adellijkeTitel_predikaat | aanduidingNaamgebruik | aanschrijfwijze                    |
            | Jonkheer                 | Eigen                 | jonkheer T. van Hoogh              |
            | Jonkvrouw                | Eigen                 | jonkvrouw T. van Hoogh             |
            | Jonkvrouw                | Partner na eigen      | jonkvrouw T. van Hoogh-in het Veld |
            | Jonkvrouw                | Partner               | T. in het Veld                     |
            | Jonkheer                 | Partner               | T. in het Veld                     |
            | Jonkvrouw                | Partner voor eigen    | T. in het Veld-jonkvrouw van Hoogh |
            | Jonkheer                 | Partner na eigen      | jonkheer T. van Hoogh-in het Veld  |
        """

        aanduiding_naamgebruik_to_enumeration = {
            "Eigen": "E",
            "Partner na eigen": "N",
            "Partner": "P",
            "Partner voor eigen": "V",
        }

        # Convert table string to rows and remove empty rows, white spaces, and header row
        table_rows = [
            [item.strip() for item in row.strip().split("|") if item]
            for row in table_string.split("\n")
            if row.strip()
        ][1:]

        voornamen = "Tom"  # Example first name to use

        for row in table_rows:
            (
                title,
                aanduiding_naamgebruik,
                aanschrijfwijze,
            ) = row

            name = aanschrijfwijze.replace("jonkheer ", "")
            name = name.replace("jonkvrouw ", "")
            last_name = None
            last_name_prefix = None
            partner_last_name_prefix = None
            partner_last_name = None
            if aanduiding_naamgebruik == "Eigen":
                last_name = name.split(" ", 1)[-1]
                if len(last_name.split(" ")) > 1:
                    split_last_name = last_name.split(" ")
                    last_name_prefix = " ".join(split_last_name[:-1])
                    last_name = split_last_name[-1]
            elif aanduiding_naamgebruik == "Partner na eigen":
                last_name = name.split(" ", 1)[-1]
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
                partner_last_name = name.split(" ", 1)[-1]
                if len(partner_last_name.split(" ")) > 1:
                    split_partner_last_name = partner_last_name.split(" ")
                    partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                    partner_last_name = split_partner_last_name[-1]
            elif aanduiding_naamgebruik == "Partner voor eigen":
                last_name = name.split(" ", 1)[-1]
                partner_last_name, last_name = last_name.split("-")
                if len(last_name.split(" ")) > 1:
                    split_last_name = last_name.split(" ")
                    last_name_prefix = " ".join(split_last_name[:-1])
                    last_name = split_last_name[-1]
                if len(partner_last_name.split(" ")) > 1:
                    split_partner_last_name = partner_last_name.split(" ")
                    partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                    partner_last_name = split_partner_last_name[-1]

            result = get_aanschrijfwijze(
                last_name_prefix,
                last_name,
                voornamen,
                partner_last_name_prefix,
                partner_last_name,
                aanduiding_naamgebruik_to_enumeration[aanduiding_naamgebruik],
                None,
                title,
                None,
            )

            self.assertEqual(aanschrijfwijze, result)


class TestGetAanschrijfwijzePartnerHasTitle(TestCase):
    def test_aanschrijfwijze_partner_has_title(self):
        table_string = """
            | geslachtsaanduiding | geslachtsaanduiding partner | adellijkeTitel_predikaat partner | aanduidingAanschrijving | samenstelling aanschrijfwijze | geslachtsnaam | voornamen      | aanschrijfwijze                         |
            | V                   | M                           | Baron                            | E                       | VL VV GN                      | Veen          | Anna Cornelia  | A.C. van der Veen                       |
            | V                   | M                           | Baron                            | N                       | VL VV GN-AP VP GP             | Veen          | Anna Cornelia  | A.C. van der Veen-barones van den Aedel |
            | V                   | M                           | Baron                            | P                       | VL AP VP GP                   | Veen          | Anna Cornelia  | A.C. barones van den Aedel              |
            | V                   | M                           | Baron                            | V                       | VL AP VP GP-VV GN             | Veen          | Anna Cornelia  | A.C. barones van den Aedel-van der Veen |
            | V                   | M                           | Prins                            | E                       | VL VV GN                      | Veen          | Anna Cornelia  | A.C. van der Veen                       |
            | V                   | M                           | Prins                            | N                       | VL VV GN-AP VP GP             | Veen          | Anna Cornelia  | A.C. van der Veen-prinses van den Aedel |
            | V                   | M                           | Prins                            | P                       | VL AP VP GP                   | Veen          | Anna Cornelia  | A.C. prinses van den Aedel              |
            | V                   | M                           | Prins                            | V                       | VL AP VP GP-VV GN             | Veen          | Anna Cornelia  | A.C. prinses van den Aedel-van der Veen |
            | M                   | V                           | Gravin                           | E                       | VL VV GN                      | Veen          | Johannes       | J. van der Veen                         |
            | M                   | V                           | Gravin                           | N                       | VL VV GN-VP GP                | Veen          | Johannes       | J. van der Veen-van den Aedel           |
            | M                   | V                           | Gravin                           | P                       | VL VP GP                      | Veen          | Johannes       | J. van den Aedel                        |
            | M                   | V                           | Gravin                           | V                       | VL VP GP-VV GN                | Veen          | Johannes       | J. van den Aedel-van der Veen           |
            | V                   | M                           | Ridder                           | E                       | VL VV GN                      | Veen          | Marlies        | M. van der Veen                         |
            | V                   | M                           | Ridder                           | N                       | VL VV GN-VP GP                | Veen          | Marlies        | M. van der Veen-van den Aedel           |
            | V                   | M                           | Ridder                           | P                       | VL VP GP                      | Veen          | Marlies        | M. van den Aedel                        |
            | V                   | M                           | Ridder                           | V                       | VL VP GP-VV GN                | Veen          | Marlies        | M. van den Aedel-van der Veen           |
            | V                   | V                           | Gravin                           | E                       | VL VV GN                      | Veen          | Sarah          | S. van der Veen                         |
            | V                   | V                           | Gravin                           | N                       | VL VV GN-VP GP                | Veen          | Sarah          | S. van der Veen-van den Aedel           |
            | V                   | V                           | Gravin                           | P                       | VL VP GP                      | Veen          | Sarah          | S. van den Aedel                        |
            | V                   | V                           | Gravin                           | V                       | VL VP GP-VV GN                | Veen          | Sarah          | S. van den Aedel-van der Veen           |
            | M                   | M                           | Baron                            | E                       | VL VV GN                      | Veen          | Willem         | W. van der Veen                         |
            | M                   | M                           | Baron                            | N                       | VL VV GN-VP GP                | Veen          | Willem         | W. van der Veen-van den Aedel           |
            | M                   | M                           | Baron                            | P                       | VL VP GP                      | Veen          | Willem         | W. van den Aedel                        |
            | M                   | M                           | Baron                            | V                       | VL VP GP-VV GN                | Veen          | Willem         | W. van den Aedel-van der Veen           |
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
                aanduiding_aanschrijving,
                _,
                last_name,
                first_name,
                aanschrijfwijze,
            ) = row

            name = aanschrijfwijze.replace("barones ", "")
            name = name.replace("prinses ", "")
            last_name = None
            last_name_prefix = None
            partner_last_name_prefix = None
            partner_last_name = None
            if aanduiding_aanschrijving == "E":
                last_name = name.split(" ", 1)[-1]
                if len(last_name.split(" ")) > 1:
                    split_last_name = last_name.split(" ")
                    last_name_prefix = " ".join(split_last_name[:-1])
                    last_name = split_last_name[-1]
            elif aanduiding_aanschrijving == "N":
                last_name = name.split(" ", 1)[-1]
                last_name, partner_last_name = last_name.split("-")
                if len(last_name.split(" ")) > 1:
                    split_last_name = last_name.split(" ")
                    last_name_prefix = " ".join(split_last_name[:-1])
                    last_name = split_last_name[-1]
                if len(partner_last_name.split(" ")) > 1:
                    split_partner_last_name = partner_last_name.split(" ")
                    partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                    partner_last_name = split_partner_last_name[-1]
            elif aanduiding_aanschrijving == "P":
                partner_last_name = name.split(" ", 1)[-1]
                if len(partner_last_name.split(" ")) > 1:
                    split_partner_last_name = partner_last_name.split(" ")
                    partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                    partner_last_name = split_partner_last_name[-1]
            elif aanduiding_aanschrijving == "V":
                last_name = name.split(" ", 1)[-1]
                partner_last_name, last_name = last_name.split("-")
                if len(last_name.split(" ")) > 1:
                    split_last_name = last_name.split(" ")
                    last_name_prefix = " ".join(split_last_name[:-1])
                    last_name = split_last_name[-1]
                if len(partner_last_name.split(" ")) > 1:
                    split_partner_last_name = partner_last_name.split(" ")
                    partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                    partner_last_name = split_partner_last_name[-1]

            result = get_aanschrijfwijze(
                last_name_prefix,
                last_name,
                first_name,
                partner_last_name_prefix,
                partner_last_name,
                aanduiding_aanschrijving,
                gender,
                None,
                partner_title,
            )

            self.assertEqual(aanschrijfwijze, result)


class TestGetAanschrijfwijzePartnerHasPredicate(TestCase):
    def test_aanschrijfwijze_person_has_title_partner_does_not(self):
        table_string = """
            | aanduidingAanschrijving | samenstelling aanschrijfwijze | geslachtsnaam | voornamen      | aanschrijfwijze            |
            | E                       | VL VV GN                      | Berg          | Sjaak          | S. van der Berg            |
            | N                       | VL VV GN-VP GP                | Berg          | Peter          | P. van der Berg-van Hoogh  |
            | P                       | VL VP GP                      | Berg          | Marlies        | M. van Hoogh               |
            | V                       | VL VP GP-VV GN                | Berg          | Fleur          | F. van Hoogh-van der Berg  |
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

            last_name_prefix = None
            partner_last_name_prefix = None
            partner_last_name = None
            if aanduiding_aanschrijving == "E":
                last_name = aanschrijfwijze.split(" ", 1)[-1]
                split_last_name = last_name.split(" ")
                last_name_prefix = " ".join(split_last_name[:-1])
            elif aanduiding_aanschrijving == "N":
                last_name = aanschrijfwijze.split(" ", 1)[-1]
                last_name, partner_last_name = last_name.split("-")
                split_last_name = last_name.split(" ")
                last_name_prefix = " ".join(split_last_name[:-1])
                split_partner_last_name = partner_last_name.split(" ")
                partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                partner_last_name = split_partner_last_name[-1]
            elif aanduiding_aanschrijving == "P":
                partner_last_name = aanschrijfwijze.split(" ", 1)[-1]
                split_partner_last_name = partner_last_name.split(" ")
                partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                partner_last_name = split_partner_last_name[-1]
            elif aanduiding_aanschrijving == "V":
                last_name = aanschrijfwijze.split(" ", 1)[-1]
                partner_last_name, last_name = last_name.split("-")
                split_last_name = last_name.split(" ")
                last_name_prefix = " ".join(split_last_name[:-1])
                split_partner_last_name = partner_last_name.split(" ")
                partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                partner_last_name = split_partner_last_name[-1]

            result = get_aanschrijfwijze(
                last_name_prefix,
                geslachtsnaam,
                voornamen,
                partner_last_name_prefix,
                partner_last_name,
                aanduiding_aanschrijving,
                None,
                None,
                None,
            )

            self.assertEqual(aanschrijfwijze, result)


class TestGetAanschrijfwijzePersonAndPartnerHasTitle(TestCase):
    def test_aanschrijfwijze_person_and_partner_has_title(self):
        table_string = """
            | aanduidingAanschrijving | samenstelling aanschrijfwijze | geslachtsnaam | voornamen      | aanschrijfwijze                             |
            | E                       | VL AT VV GN                   | Aedel         | Hendrik Willem | H.W. graaf van den Aedel                    |
            | N                       | VL AT VV GN-AP VP GP          | Aedel         | Wilhelmina     | W. gravin van den Aedel-barones van Hoogh   |
            | P                       | VL AP VP GP                   | Aedel         | Frederique     | F. barones van Hoogh                        |
            | V                       | VL AP VP GP-AT VV GN          | Aedel         | Emma Louise    | E.L. barones van Hoogh-gravin van den Aedel |
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

            last_name_prefix = None
            partner_last_name_prefix = None
            partner_last_name = None
            if aanduiding_aanschrijving == "E":
                last_name = aanschrijfwijze.split(" ", 1)[-1]
                split_last_name = last_name.split(" ")
                last_name_prefix = " ".join(split_last_name[:-1])
            elif aanduiding_aanschrijving == "N":
                last_name = aanschrijfwijze.split(" ", 1)[-1]
                last_name, partner_last_name = last_name.split("-")
                split_last_name = last_name.split(" ")
                last_name_prefix = " ".join(split_last_name[:-1])
                split_partner_last_name = partner_last_name.split(" ")
                partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                partner_last_name = split_partner_last_name[-1]
            elif aanduiding_aanschrijving == "P":
                partner_last_name = aanschrijfwijze.split(" ", 1)[-1]
                split_partner_last_name = partner_last_name.split(" ")
                partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                partner_last_name = split_partner_last_name[-1]
            elif aanduiding_aanschrijving == "V":
                last_name = aanschrijfwijze.split(" ", 1)[-1]
                partner_last_name, last_name = last_name.split("-")
                split_last_name = last_name.split(" ")
                last_name_prefix = " ".join(split_last_name[:-1])
                split_partner_last_name = partner_last_name.split(" ")
                partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                partner_last_name = split_partner_last_name[-1]

            result = get_aanschrijfwijze(
                last_name_prefix,
                geslachtsnaam,
                voornamen,
                partner_last_name_prefix,
                partner_last_name,
                aanduiding_aanschrijving,
                None,
                None,
                None,
            )

            self.assertEqual(aanschrijfwijze, result)
