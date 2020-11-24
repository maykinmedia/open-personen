from django.test import TestCase

from openpersonen.features import get_aanhef


class TestAanhefWithOnlyGenderDesignation(TestCase):
    def test_aanhef_with_female_gender_designation(self):
        result = get_aanhef("van", "Jong", "V", None, None)

        self.assertEqual(result, "Geachte mevrouw Van Jong")

    def test_aanhef_with_male_gender_designation(self):
        result = get_aanhef(None, "Jong", "M", None, None)

        self.assertEqual(result, "Geachte heer Jong")

    def test_aanhef_with_no_gender_designation(self):
        result = get_aanhef(None, None, "", None, None)

        self.assertEqual(result, "string")


class TestAanhefWithTitle(TestCase):
    def test_aanhef_with_baron_title(self):
        result = get_aanhef(None, None, None, "Baron", None)

        self.assertEqual(result, "Geachte Hoogwelgeboren heer")

    def test_aanhef_with_barones_title(self):
        result = get_aanhef(None, None, None, "Barones", None)

        self.assertEqual(result, "Geachte Hoogwelgeboren vrouwe")

    def test_aanhef_with_graaf_title(self):
        result = get_aanhef(None, None, None, "Graaf", None)

        self.assertEqual(result, "Geachte Hooggeboren heer")

    def test_aanhef_with_gravin_title(self):
        result = get_aanhef(None, None, None, "Gravin", None)

        self.assertEqual(result, "Geachte Hooggeboren vrouwe")

    def test_aanhef_with_hertog_title(self):
        result = get_aanhef(None, None, None, "Hertog", None)

        self.assertEqual(result, "Geachte Hoogwelgeboren heer")

    def test_aanhef_with_hertogin_title(self):
        result = get_aanhef(None, None, None, "Hertogin", None)

        self.assertEqual(result, "Geachte Hoogwelgeboren vrouwe")

    def test_aanhef_with_jonkheer_title(self):
        result = get_aanhef(None, None, None, "Jonkheer", None)

        self.assertEqual(result, "Geachte Hoogwelgeboren heer")

    def test_aanhef_with_jonkvrouw_title(self):
        result = get_aanhef(None, None, None, "Jonkvrouw", None)

        self.assertEqual(result, "Geachte Hoogwelgeboren vrouwe")

    def test_aanhef_with_markies_title(self):
        result = get_aanhef(None, None, None, "Markies", None)

        self.assertEqual(result, "Geachte Hoogwelgeboren heer")

    def test_aanhef_with_markiezin_title(self):
        result = get_aanhef(None, None, None, "Markiezin", None)

        self.assertEqual(result, "Geachte Hoogwelgeboren vrouwe")

    def test_aanhef_with_prins_title(self):
        result = get_aanhef(None, None, None, "Prins", None)

        self.assertEqual(result, "Geachte Hoogheid")

    def test_aanhef_with_prinses_title(self):
        result = get_aanhef(None, None, None, "Prinses", None)

        self.assertEqual(result, "Geachte Hoogheid")

    def test_aanhef_with_ridder_title(self):
        result = get_aanhef(None, None, None, "Ridder", None)

        self.assertEqual(result, "Geachte Hoogwelgeboren heer")


class TestAanhefWithPartnerTitle(TestCase):
    def test_aanhef_with_partner_baron_title(self):
        result = get_aanhef(None, None, None, None, "Baron")

        self.assertEqual(result, "Geachte Hoogwelgeboren vrouwe")

    def test_aanhef_with_partner_graaf_title(self):
        result = get_aanhef(None, None, None, None, "Graaf")

        self.assertEqual(result, "Geachte Hooggeboren vrouwe")

    def test_aanhef_with_partner_hertog_title(self):
        result = get_aanhef(None, None, None, None, "Hertog")

        self.assertEqual(result, "Geachte Hoogwelgeboren vrouwe")

    def test_aanhef_with_partner_markies_title(self):
        result = get_aanhef(None, None, None, None, "Markies")

        self.assertEqual(result, "Geachte Hoogwelgeboren vrouwe")

    def test_aanhef_with_partner_prins_title(self):
        result = get_aanhef(None, None, None, None, "Prins")

        self.assertEqual(result, "Geachte Hoogheid")


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

        # Convert table string to rows and remove empty rows, white spaces, and header row
        table_rows = [
            [item.strip() for item in row.strip().split("|") if item]
            for row in table_string.split("\n")
            if row.strip()
        ][1:]
