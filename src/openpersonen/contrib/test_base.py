from django.test import TestCase

from openpersonen.contrib.base import BaseBackend


class TestBaseBackend(TestCase):
    def setUp(self):
        self.base_backend = BaseBackend()
        self.bsn = 123456789
        self.filters = {"fake": "filter"}

    def test_get_person_raises_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            self.base_backend.get_person(bsn=self.bsn)

    def test_get_kind_raises_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            self.base_backend.get_kind(self.bsn)

    def test_get_ouder_raises_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            self.base_backend.get_ouder(self.bsn)

    def test_get_partner_raises_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            self.base_backend.get_partner(self.bsn)

    def test_get_nationaliteit_historie_raises_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            self.base_backend.get_nationaliteit_historie(self.bsn, self.filters)

    def test_get_partner_historie_raises_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            self.base_backend.get_partner_historie(self.bsn, self.filters)

    def test_get_verblijf_plaats_historie_raises_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            self.base_backend.get_verblijf_plaats_historie(self.bsn, self.filters)

    def test_get_verblijfs_titel_historie_raises_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            self.base_backend.get_verblijfs_titel_historie(self.bsn, self.filters)
