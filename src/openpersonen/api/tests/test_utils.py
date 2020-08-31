from collections import OrderedDict

from django.test import TestCase

from openpersonen.api.utils import convert_empty_instances


class TestConvertEmptyInstances(TestCase):
    def test_convert_empty_instances(self):
        original_dict = {
            "key": OrderedDict(),
            "nested_dict": {"nested_key": OrderedDict(),},
        }
        expected_dict = {
            "key": None,
            "nested_dict": {"nested_key": None,},
        }

        convert_empty_instances(original_dict)

        self.assertEqual(original_dict, expected_dict)
