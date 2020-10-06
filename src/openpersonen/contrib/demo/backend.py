from django.apps import apps

from openpersonen.contrib.demo.converters import *


class BackEnd:
    # Note: All methods must return a list of dicts

    @staticmethod
    def _update_filters_to_fit_model(filters):
        query_param_to_model_field_mapping = {
            "geboorte__datum": "geboortedatum_persoon",
            "verblijfplaats__gemeentevaninschrijving": "verblijfplaats__gemeente_van_inschrijving",
            "naam__geslachtsnaam": "geslachtsnaam_persoon",
            "burgerservicenummer": "burgerservicenummer_persoon",
            "verblijfplaats__naamopenbareruimte": "verblijfplaats__naam_openbare_ruimte",
            "verblijfplaats__identificatiecodenummeraanduiding": "verblijfplaats__identificatiecode_nummeraanduiding",
        }

        for (
            query_param_key,
            model_field_key,
        ) in query_param_to_model_field_mapping.items():
            if query_param_key in filters:
                filters[model_field_key] = filters.pop(query_param_key)

    def get_person(self, bsn=None, filters=None):
        if not bsn and not filters:
            raise ValueError("Either bsn or filters must be supplied")

        Persoon = apps.get_model("demo", "Persoon")

        if filters:
            self._update_filters_to_fit_model(filters)
            instances = Persoon.objects.filter(**filters)
        else:
            instances = Persoon.objects.filter(burgerservicenummer_persoon=bsn)

        instance_dicts = []
        for instance in instances:
            instance_dicts.append(convert_persoon_to_instance_dict(instance))

        return instance_dicts

    def get_kind(self, bsn, id=None):

        Persoon = apps.get_model("demo", "Persoon")

        if id:
            instances = Persoon.objects.get(
                burgerservicenummer_persoon=bsn
            ).kind_set.filter(burgerservicenummer_kind=id)
        else:
            instances = Persoon.objects.get(
                burgerservicenummer_persoon=bsn
            ).kind_set.all()

        instance_dicts = []
        for instance in instances:
            instance_dicts.append(convert_kind_to_instance_dict(instance))

        return instance_dicts

    def get_ouder(self, bsn, id=None):
        Persoon = apps.get_model("demo", "Persoon")

        if id:
            instances = Persoon.objects.get(
                burgerservicenummer_persoon=bsn
            ).ouder_set.filter(burgerservicenummer_ouder=id)
        else:
            instances = Persoon.objects.get(
                burgerservicenummer_persoon=bsn
            ).ouder_set.all()

        instance_dicts = []
        for instance in instances:
            instance_dicts.append(convert_ouder_instance_to_dict(instance))

        return instance_dicts

    def get_partner(self, bsn, id=None):
        Persoon = apps.get_model("demo", "Persoon")

        if id:
            instances = Persoon.objects.get(
                burgerservicenummer_persoon=bsn
            ).partnerschap_set.filter(
                burgerservicenummer_echtgenoot_geregistreerd_partner=id
            )
        else:
            instances = Persoon.objects.get(
                burgerservicenummer_persoon=bsn
            ).partnerschap_set.all()

        instance_dicts = []
        for instance in instances:
            instance_dicts.append(convert_partner_instance_to_dict(instance))

        return instance_dicts
