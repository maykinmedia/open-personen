from django.test import TestCase

from openpersonen.features import get_aanhef


class TestAanhefWithOnlyGenderDesignation(TestCase):
    def test_aanhef_with_female_gender_designation(self):
        result = get_aanhef("van", "Jong", None, None, "E", "V", None, None)

        self.assertEqual(result, "Geachte mevrouw Van Jong")

    def test_aanhef_with_male_gender_designation(self):
        result = get_aanhef(None, "Jong", None, None, "E", "M", None, None)

        self.assertEqual(result, "Geachte heer Jong")

    def test_aanhef_with_no_gender_designation(self):
        result = get_aanhef(None, None, None, None, None, "", None, None)

        self.assertEqual(result, "string")


class TestAanhefWithTitle(TestCase):
    def test_aanhef_with_baron_title(self):
        result = get_aanhef(None, None, None, None, None, None, "Baron", None)

        self.assertEqual(result, "Hoogwelgeboren heer")

    def test_aanhef_with_barones_title(self):
        result = get_aanhef(None, None, None, None, None, None, "Barones", None)

        self.assertEqual(result, "Hoogwelgeboren vrouwe")

    def test_aanhef_with_graaf_title(self):
        result = get_aanhef(None, None, None, None, None, None, "Graaf", None)

        self.assertEqual(result, "Hooggeboren heer")

    def test_aanhef_with_gravin_title(self):
        result = get_aanhef(None, None, None, None, None, None, "Gravin", None)

        self.assertEqual(result, "Hooggeboren vrouwe")

    def test_aanhef_with_hertog_title(self):
        result = get_aanhef(None, None, None, None, None, None, "Hertog", None)

        self.assertEqual(result, "Hoogwelgeboren heer")

    def test_aanhef_with_hertogin_title(self):
        result = get_aanhef(None, None, None, None, None, None, "Hertogin", None)

        self.assertEqual(result, "Hoogwelgeboren vrouwe")

    def test_aanhef_with_jonkheer_title(self):
        result = get_aanhef(None, None, None, None, None, None, "Jonkheer", None)

        self.assertEqual(result, "Hoogwelgeboren heer")

    def test_aanhef_with_jonkvrouw_title(self):
        result = get_aanhef(None, None, None, None, "E", None, "Jonkvrouw", None)

        self.assertEqual(result, "Hoogwelgeboren vrouwe")

    def test_aanhef_with_markies_title(self):
        result = get_aanhef(None, None, None, None, None, None, "Markies", None)

        self.assertEqual(result, "Hoogwelgeboren heer")

    def test_aanhef_with_markiezin_title(self):
        result = get_aanhef(None, None, None, None, None, None, "Markiezin", None)

        self.assertEqual(result, "Hoogwelgeboren vrouwe")

    def test_aanhef_with_prins_title(self):
        result = get_aanhef(None, None, None, None, None, None, "Prins", None)

        self.assertEqual(result, "Hoogheid")

    def test_aanhef_with_prinses_title(self):
        result = get_aanhef(None, None, None, None, None, None, "Prinses", None)

        self.assertEqual(result, "Hoogheid")

    def test_aanhef_with_ridder_title(self):
        result = get_aanhef(None, None, None, None, None, None, "Ridder", None)

        self.assertEqual(result, "Hoogwelgeboren heer")


class TestAanhefWithPartnerTitle(TestCase):
    def test_aanhef_with_partner_baron_title(self):
        result = get_aanhef(None, None, None, None, None, "V", None, "Baron")

        self.assertEqual(result, "Hoogwelgeboren vrouwe")

    def test_aanhef_with_partner_graaf_title(self):
        result = get_aanhef(None, None, None, None, None, "V", None, "Graaf")

        self.assertEqual(result, "Hooggeboren vrouwe")

    def test_aanhef_with_partner_hertog_title(self):
        result = get_aanhef(None, None, None, None, None, "V", None, "Hertog")

        self.assertEqual(result, "Hoogwelgeboren vrouwe")

    def test_aanhef_with_partner_markies_title(self):
        result = get_aanhef(None, None, None, None, None, "V", None, "Markies")

        self.assertEqual(result, "Hoogwelgeboren vrouwe")

    def test_aanhef_with_partner_prins_title(self):
        result = get_aanhef(None, None, None, None, None, "V", None, "Prins")

        self.assertEqual(result, "Hoogheid")


class TestGetAanHefWithoutTitle(TestCase):
    def test_aanhef_without_title(self):
        """
        Testing examples given here: https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/aanhef.feature
        """
        table_string = """
            | aanduidingNaamgebruik | geslachtsaanduiding |samenstelling aanhef | aanschrijfwijze           | aanhef                                 |
            | Eigen                 | Man                 | GA VV GN            | H. in het Veld            | Geachte heer In het Veld               |
            | Eigen                 | Man                 | GA VV GN            | F. Groenen                | Geachte heer Groenen                   |
            | Partner na eigen      | Vrouw               | GA VV GN-VP GP      | I. van Velzen-in het Veld | Geachte mevrouw Van Velzen-in het Veld |
            | Partner na eigen      | Vrouw               | GA VV GN-VP GP      | F. Groenen-Groenink       | Geachte mevrouw Groenen-Groenink       |
            | Partner               | Vrouw               | GA VP GP            | S. van Velzen             | Geachte mevrouw Van Velzen             |
            | Partner               | Vrouw               | GA VP GP            | J.F.R. Groenen            | Geachte mevrouw Groenen                |
            | Partner voor eigen    | Man                 | GA VP GP-VV GN      | F. in het Veld-van Velzen | Geachte heer In het Veld-van Velzen    |
            | Partner voor eigen    | Man                 | GA VP GP-VV GN      | F. Groenen-Groenink       | Geachte heer Groenen-Groenink          |
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
                aanduiding_naamgebruik,
                geslachtsaanduiding,
                _,
                aanschrijfwijze,
                aanhef,
            ) = row

            last_name_prefix = None
            last_name = None
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

            result = get_aanhef(
                last_name_prefix,
                last_name,
                partner_last_name_prefix,
                partner_last_name,
                aanduiding_naamgebruik_to_enumeration[aanduiding_naamgebruik],
                geslachtsaanduiding_to_enumeration[geslachtsaanduiding],
                None,
                None,
            )
            self.assertEqual(aanhef, result)


class TestGetAanHefWithCapitalOrSmallLetters(TestCase):
    def test_get_aanhef_with_capital_or_small_letters(self):
        """
        Testing examples given here: https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/aanhef.feature#L109-L114
        """
        table_string = """
            | aanduidingNaamgebruik | geslachtsaanduiding |samenstelling aanhef | aanschrijfwijze           | aanhef                                 |
            | Eigen                 | Man                 | GA VV GN            | H. in het Veld            | Geachte heer In het Veld               |
            | Eigen                 | Man                 | GA VV GN            | F. Groenen                | Geachte heer Groenen                   |
            | Partner na eigen      | Vrouw               | GA VV GN-VP GP      | I. van Velzen-in het Veld | Geachte mevrouw Van Velzen-in het Veld |
            | Partner na eigen      | Vrouw               | GA VV GN-VP GP      | F. Groenen-Groenink       | Geachte mevrouw Groenen-Groenink       |
            | Partner               | Vrouw               | GA VP GP            | S. van Velzen             | Geachte mevrouw Van Velzen             |
            | Partner               | Vrouw               | GA VP GP            | J.F.R. Groenen            | Geachte mevrouw Groenen                |
            | Partner voor eigen    | Man                 | GA VP GP-VV GN      | F. in het Veld-van Velzen | Geachte heer In het Veld-van Velzen    |
            | Partner voor eigen    | Man                 | GA VP GP-VV GN      | F. Groenen-Groenink       | Geachte heer Groenen-Groenink          |
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
                aanduiding_naamgebruik,
                geslachtsaanduiding,
                _,
                aanschrijfwijze,
                aanhef,
            ) = row

            last_name_prefix = None
            last_name = None
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

            result = get_aanhef(
                last_name_prefix,
                last_name,
                partner_last_name_prefix,
                partner_last_name,
                aanduiding_naamgebruik_to_enumeration[aanduiding_naamgebruik],
                geslachtsaanduiding_to_enumeration[geslachtsaanduiding],
                None,
                None,
            )
            self.assertEqual(aanhef, result)


class TestGetAanHefWithTitle(TestCase):
    def test_get_aanhef_with_title(self):
        table_string = """
            | adellijkeTitel_predikaat | aanduidingNaamgebruik | aanschrijfwijze                             | aanhef                    |
            | Baron                    | Eigen                 | H.W. baron van den Aedel                    | Hoogwelgeboren heer       |
            | Barones                  | Partner na eigen      | W. barones van den Aedel-van der Veen       | Hoogwelgeboren vrouwe     |
            | Graaf                    | Partner               | F. van der Veen                             | Geachte heer Van der Veen |
            | Gravin                   | Partner voor eigen    | E.L. van der Veen-gravin van den Aedel      | Hooggeboren vrouwe        |
            | Prins                    | Eigen                 | O.B.B. prins van Roodt de Wit Blaauw        | Hoogheid                  |
            | Prinses                  | Eigen                 | E.M.V. prinses van Roodt de Wit Blaauw      | Hoogheid                  |
            | Ridder                   | Eigen                 | M. ridder van Hoogh                         | Hoogwelgeboren heer       |
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

        for row in table_rows:
            (
                adellijke_titel_predikaat,
                aanduiding_naamgebruik,
                aanschrijfwijze,
                aanhef,
            ) = row

            gender_designation = None

            if "heer" in aanhef:
                gender_designation = "M"
            if "vrouwe" in aanhef:
                gender_designation = "V"

            last_name_prefix = None
            last_name = None
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

            result = get_aanhef(
                last_name_prefix,
                last_name,
                partner_last_name_prefix,
                partner_last_name,
                aanduiding_naamgebruik_to_enumeration[aanduiding_naamgebruik],
                gender_designation,
                adellijke_titel_predikaat,
                None,
            )
            self.assertEqual(aanhef, result)


class TestGetAanHefWithPredikaat(TestCase):
    def test_get_aanhef_with_predikaat(self):
        table_string = """
            | adellijkeTitel_predikaat | aanduidingNaamgebruik | partner | Ontbinding huwelijk/geregistreerd partnerschap | aanhef                                 |
            | Jonkheer                 | Eigen                 | Geen    | Geen                                           | Hoogwelgeboren heer                    |
            | Jonkheer                 | Eigen                 | Ja      | Geen                                           | Hoogwelgeboren heer                    |
            | Jonkheer                 | Partner na eigen      | Ja      | Geen                                           | Hoogwelgeboren heer                    |
            | Jonkheer                 | Partner               | Ja      | Geen                                           | Hoogwelgeboren heer                    |
            | Jonkheer                 | Partner voor eigen    | Ja      | Geen                                           | Hoogwelgeboren heer                    |
            | Jonkvrouw                | Eigen                 | Geen    | Geen                                           | Hoogwelgeboren vrouwe                  |
            | Jonkvrouw                | Eigen                 | Ja      | Geen                                           | Geachte mevrouw Van Hoogh              |
            | Jonkvrouw                | Partner na eigen      | Ja      | Geen                                           | Geachte mevrouw Van Hoogh-van der Veen |
            | Jonkvrouw                | Partner               | Ja      | Geen                                           | Geachte mevrouw Van der Veen-van Hoogh |
            | Jonkvrouw                | Partner voor eigen    | Ja      | Geen                                           | Geachte mevrouw Van der Veen           |
            | Jonkvrouw                | Eigen                 | Ja      | Ja                                             | Hoogwelgeboren vrouwe                  |
            | Jonkvrouw                | Partner na eigen      | Ja      | Ja                                             | Geachte mevrouw Van Hoogh-van der Veen |
            | Jonkvrouw                | Partner               | Ja      | Ja                                             | Geachte mevrouw Van der Veen-van Hoogh |
            | Jonkvrouw                | Partner voor eigen    | Ja      | Ja                                             | Geachte mevrouw Van der Veen           |
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

        for row in table_rows:
            (
                adellijke_titel_predikaat,
                aanduiding_naamgebruik,
                has_partner,
                is_dissolved,
                aanhef,
            ) = row

            last_name = aanhef
            for title in [
                "Hoogwelgeboren heer",
                "Hoogwelgeboren vrouwe",
                "Geachte mevrouw ",
            ]:
                last_name = last_name.replace(title, "")

            gender_designation = None

            if "heer" in aanhef:
                gender_designation = "M"
            if "mevrouw" in aanhef:
                gender_designation = "V"

            last_name_prefix = None
            partner_last_name_prefix = None
            partner_last_name = None

            if last_name and aanduiding_naamgebruik == "Eigen":
                if len(last_name.split(" ")) > 1:
                    split_last_name = last_name.split(" ")
                    last_name_prefix = " ".join(split_last_name[:-1])
                    last_name = split_last_name[-1]
                if has_partner == "Ja":
                    partner_last_name = last_name
            elif last_name and aanduiding_naamgebruik == "Partner na eigen":
                last_name, partner_last_name = last_name.split("-")
                if len(last_name.split(" ")) > 1:
                    split_last_name = last_name.split(" ")
                    last_name_prefix = " ".join(split_last_name[:-1])
                    last_name = split_last_name[-1]
                if len(partner_last_name.split(" ")) > 1:
                    split_partner_last_name = partner_last_name.split(" ")
                    partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                    partner_last_name = split_partner_last_name[-1]
            elif last_name and aanduiding_naamgebruik == "Partner":
                partner_last_name = last_name
                last_name = None
                last_name_prefix = None
            elif last_name and aanduiding_naamgebruik == "Partner voor eigen":
                if len(last_name.split("-")) > 1:
                    partner_last_name, last_name = last_name.split("-")
                if len(last_name.split(" ")) > 1:
                    split_last_name = last_name.split(" ")
                    last_name_prefix = " ".join(split_last_name[:-1])
                    last_name = split_last_name[-1]
                if partner_last_name and len(partner_last_name.split(" ")) > 1:
                    split_partner_last_name = partner_last_name.split(" ")
                    partner_last_name_prefix = " ".join(split_partner_last_name[:-1])
                    partner_last_name = split_partner_last_name[-1]
                if not partner_last_name:
                    partner_last_name = ""
                    partner_last_name_prefix = ""

            result = get_aanhef(
                last_name_prefix,
                last_name,
                partner_last_name_prefix,
                partner_last_name,
                aanduiding_naamgebruik_to_enumeration[aanduiding_naamgebruik],
                gender_designation,
                adellijke_titel_predikaat,
                None,
            )
            self.assertEqual(aanhef, result)


class TestGetAanHefWithAdelijkeTitelOfPredikaat(TestCase):
    def test_get_aanhef_with_adelijke_titel_of_predikaat(self):
        table_string = """
              | geslachtsaanduiding | geslachtsaanduiding partner | adellijkeTitel_predikaat partner | aanduidingNaamgebruik | aanschrijfwijze                         | aanhef                                     |
              | V                   | M                           | Baron                            | Eigen                 | A.C. van der Veen                       | Geachte mevrouw Van der Veen               |
              | V                   | M                           | Baron                            | Partner na eigen      | A.C. van der Veen-barones van den Aedel | Hoogwelgeboren vrouwe                      |
              | V                   | M                           | Baron                            | Partner               | A.C. barones van den Aedel              | Hoogwelgeboren vrouwe                      |
              | V                   | M                           | Baron                            | Partner voor eigen    | A.C. barones van den Aedel-van der Veen | Hoogwelgeboren vrouwe                      |
              | M                   | V                           | Gravin                           | Eigen                 | W. van der Veen                         | Geachte heer Van der Veen                  |
              | M                   | V                           | Gravin                           | Partner na eigen      | W. van der Veen-van den Aedel           | Geachte heer Van der Veen-van den Aedel    |
              | M                   | V                           | Gravin                           | Partner               | W. van den Aedel                        | Geachte heer Van den Aedel                 |
              | M                   | V                           | Gravin                           | Partner voor eigen    | W. van den Aedel-van der Veen           | Geachte heer Van den Aedel-van der Veen    |
              | M                   | M                           | Baron                            | Partner na eigen      | W. van der Veen-van den Aedel           | Geachte heer Van der Veen-van den Aedel    |
              | V                   | V                           | Barones                          | Partner na eigen      | W. van der Veen-van den Aedel           | Geachte mevrouw Van der Veen-van den Aedel |
              | V                   | M                           | Ridder                           | Partner na eigen      | W. van der Veen-van den Aedel           | Geachte mevrouw Van der Veen-van den Aedel |
              | V                   | M                           | Ridder                           | Partner               | W. van den Aedel                        | Geachte mevrouw Van den Aedel              |
              | V                   | M                           | Jonkheer                         | Eigen                 | A.C. van der Veen                       | Geachte mevrouw Van der Veen               |
              | V                   | M                           | Jonkheer                         | Partner na eigen      | A.C. van der Veen-van den Aedel         | Geachte mevrouw Van der Veen-van den Aedel |
              | V                   | M                           | Jonkheer                         | Partner               | A.C. van den Aedel                      | Geachte mevrouw Van den Aedel              |
              | V                   | M                           | Jonkheer                         | Partner voor eigen    | A.C. van den Aedel-van der Veen         | Geachte mevrouw Van den Aedel-van der Veen |
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

        for row in table_rows:
            (
                gender_designation,
                geslachtsaanduiding_partner,
                adelijke_title_predikaat_partner,
                aanduiding_naamgebruik,
                aanschrijfwijze,
                aanhef,
            ) = row

            last_name = aanhef
            for title in [
                "Hoogwelgeboren heer",
                "Hoogwelgeboren vrouwe",
                "Geachte mevrouw ",
            ]:
                last_name = last_name.replace(title, "")

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

            result = get_aanhef(
                last_name_prefix,
                last_name,
                partner_last_name_prefix,
                partner_last_name,
                aanduiding_naamgebruik_to_enumeration[aanduiding_naamgebruik],
                gender_designation,
                None,
                adelijke_title_predikaat_partner,
            )
            self.assertEqual(aanhef, result)
