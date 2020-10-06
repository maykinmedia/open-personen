from django.apps import apps

from openpersonen.contrib.demo.converters import convert_persoon_to_instance_dict


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

    def get_kind(self, bsn, kind_bsn=None):

        Persoon = apps.get_model("demo", "Persoon")

        if kind_bsn:
            return Persoon.objects.get(burgerservicenummer_persoon=bsn).kind_set.get(
                burgerservicenummer_kind=kind_bsn
            )
        else:
            return Persoon.objects.get(burgerservicenummer_persoon=bsn).kind_set.all()

    def get_ouder(self, bsn, ouder_bsn=None):
        Persoon = apps.get_model("demo", "Persoon")

        if ouder_bsn:
            return Persoon.objects.get(burgerservicenummer_persoon=bsn).ouder_set.get(
                burgerservicenummer_ouder=ouder_bsn
            )
        else:
            return Persoon.objects.get(burgerservicenummer_persoon=bsn).ouder_set.all()

    def get_partner(self, bsn, partner_bsn=None):
        Persoon = apps.get_model("demo", "Persoon")

        if partner_bsn:
            return Persoon.objects.get(
                burgerservicenummer_persoon=bsn
            ).partnerschap_set.get(
                burgerservicenummer_echtgenoot_geregistreerd_partner=partner_bsn
            )
        else:
            return Persoon.objects.get(
                burgerservicenummer_persoon=bsn
            ).partnerschap_set.all()
