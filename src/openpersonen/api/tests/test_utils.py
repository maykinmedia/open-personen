from collections import OrderedDict

from django.test import TestCase

from openpersonen.api.utils import convert_empty_instances, is_expected_date_format


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


class TestIsExpectedDateFormat(TestCase):
    def test_is_expected_date_format_returns_true_with_correct_date_format(self):
        date = "19801223"
        result = is_expected_date_format(date)
        self.assertTrue(result)

    def test_is_expected_date_format_returns_false_with_incorrect_date_format(self):
        date = "19800000"
        result = is_expected_date_format(date)
        self.assertFalse(result)
