from collections import OrderedDict

from django.test import TestCase

from freezegun import freeze_time

from openpersonen.api.utils import (
    calculate_age,
    convert_empty_instances,
    is_valid_date_format,
)


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
        birth_date = "19750101"
        result = calculate_age(birth_date)
        self.assertEqual(result, 45)

    @freeze_time("2020-09-12")
    def test_calculate_age_with_just_year(self):
        birth_date = "19610000"
        result = calculate_age(birth_date)
        self.assertEqual(result, 59)

    @freeze_time("2020-09-12")
    def test_calculate_age_with_no_data(self):
        birth_date = ""
        result = calculate_age(birth_date)
        self.assertEqual(result, 0)


class TestIsValidDateFormat(TestCase):
    def test_is_valid_date_format_returns_true(self):
        date = "19750816"
        result = is_valid_date_format(date)
        self.assertTrue(result)

    def test_is_valid_date_format_returns_false_when_too_short(self):
        date = "1975"
        result = is_valid_date_format(date)
        self.assertFalse(result)

    def test_is_valid_date_format_returns_false_when_not_a_number(self):
        date = "A"
        result = is_valid_date_format(date)
        self.assertFalse(result)
