from django.test import TestCase
from openpersonen.features import get_aanhef


class TestAanhefWithOnlyGenderDesignation(TestCase):

    def test_aanhef_with_female_gender_designation(self):
        result = get_aanhef({'geslachtsaanduiding': 'V'}, None)

        self.assertEqual(result, 'mevrouw')

    def test_aanhef_with_male_gender_designation(self):
        result = get_aanhef({'geslachtsaanduiding': 'M'}, None)

        self.assertEqual(result, 'heer')

    def test_aanhef_with_no_gender_designation(self):
        result = get_aanhef({'geslachtsaanduiding': ''}, None)

        self.assertEqual(result, 'string')


class TestAanhefWithTitle(TestCase):

    def test_aanhef_with_baron_title(self):
        result = get_aanhef({}, 'Baron')

        self.assertEqual(result, 'Hoogwelgeboren heer')

    def test_aanhef_with_barones_title(self):
        result = get_aanhef({}, 'Barones')

        self.assertEqual(result, 'Hoogwelgeboren vrouwe')

    def test_aanhef_with_graaf_title(self):
        result = get_aanhef({}, 'Graaf')

        self.assertEqual(result, 'Hooggeboren heer')

    def test_aanhef_with_gravin_title(self):
        result = get_aanhef({}, 'Gravin')

        self.assertEqual(result, 'Hooggeboren vrouwe')

    def test_aanhef_with_hertog_title(self):
        result = get_aanhef({}, 'Hertog')

        self.assertEqual(result, 'Hoogwelgeboren heer')

    def test_aanhef_with_hertogin_title(self):
        result = get_aanhef({}, 'Hertogin')

        self.assertEqual(result, 'Hoogwelgeboren vrouwe')

    def test_aanhef_with_jonkheer_title(self):
        result = get_aanhef({}, 'Jonkheer')

        self.assertEqual(result, 'Hoogwelgeboren heer')

    def test_aanhef_with_jonkvrouw_title(self):
        result = get_aanhef({}, 'Jonkvrouw')

        self.assertEqual(result, 'Hoogwelgeboren vrouwe')

    def test_aanhef_with_markies_title(self):
        result = get_aanhef({}, 'Markies')

        self.assertEqual(result, 'Hoogwelgeboren heer')

    def test_aanhef_with_markiezin_title(self):
        result = get_aanhef({}, 'Markiezin')

        self.assertEqual(result, 'Hoogwelgeboren vrouwe')

    def test_aanhef_with_prins_title(self):
        result = get_aanhef({}, 'Prins')

        self.assertEqual(result, 'Hoogheid')


    def test_aanhef_with_prinses_title(self):
        result = get_aanhef({}, 'Prinses')

        self.assertEqual(result, 'Hoogheid')

    def test_aanhef_with_ridder_title(self):
        result = get_aanhef({}, 'Ridder')

        self.assertEqual(result, 'Hoogwelgeboren heer')
