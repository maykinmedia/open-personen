from collections import OrderedDict

from freezegun import freeze_time

from django.test import TestCase

from openpersonen.api.utils import convert_empty_instances, calculate_age


class TestConvertEmptyInstances(TestCase):
    def test_convert_empty_instances(self):
        original_dict = {
            "key": OrderedDict(),
            "nested_dict": {
                "nested_key": OrderedDict(),
            },
        }
        expected_dict = {
            "key": None,
            "nested_dict": {
                "nested_key": None,
            },
        }

        convert_empty_instances(original_dict)

        self.assertEqual(original_dict, expected_dict)


class TestCalculateAge(TestCase):

    @freeze_time("2020-09-12")
    def test_calculate_age_with_full_date(self):
        birth_date = '19750101'
        result = calculate_age(birth_date)
        self.assertEqual(result, 45)

    @freeze_time("2020-09-12")
    def test_calculate_age_with_just_year(self):
        birth_date = '19610000'
        result = calculate_age(birth_date)
        self.assertEqual(result, 59)

    @freeze_time("2020-09-12")
    def test_calculate_age_with_no_data(self):
        birth_date = ''
        result = calculate_age(birth_date)
        self.assertEqual(result, 0)
