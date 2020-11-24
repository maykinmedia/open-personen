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
