from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ViewSet

from openpersonen.api.filters import Backend, IngeschrevenPersoonFilter
from openpersonen.contrib.stufbg.models import StufBGClient


class IngeschrevenPersoonViewSet(ViewSet):

    lookup_field = "burgerservicenummer"
    lookup_value_regex = "[0-9]{9}"
    filter_class = IngeschrevenPersoonFilter

    @staticmethod
    def combination_1(filters_values_dict):
        return (
            len(filters_values_dict) == 2
            and "geboorte__datum" in filters_values_dict
            and "naam__geslachtsnaam" in filters_values_dict
            and len(filters_values_dict["naam__geslachtsnaam"]) > 1
        )

    @staticmethod
    def combination_2(filters_values_dict):
        return (
            len(filters_values_dict) == 2
            and "verblijfplaats__gemeentevaninschrijving" in filters_values_dict
            and "naam__geslachtsnaam" in filters_values_dict
            and len(filters_values_dict["naam__geslachtsnaam"]) > 1
        )

    @staticmethod
    def combination_3(filters_values_dict):
        return (
            len(filters_values_dict) == 1
            and "burgerservicenummer" in filters_values_dict
        )

    @staticmethod
    def combination_4(filters_values_dict):
        return (
            len(filters_values_dict) == 2
            and "verblijfplaats__postcode" in filters_values_dict
            and "verblijfplaats__huisnummer" in filters_values_dict
        )

    @staticmethod
    def combination_5(filters_values_dict):
        return (
            len(filters_values_dict) == 3
            and "verblijfplaats__gemeentevaninschrijving" in filters_values_dict
            and "verblijfplaats__huisnummer" in filters_values_dict
            and "verblijfplaats__naamopenbareruimte" in filters_values_dict
            and len(filters_values_dict["verblijfplaats__naamopenbareruimte"]) > 1
        )

    @staticmethod
    def combination_6(filters_values_dict):
        return (
            len(filters_values_dict) == 1
            and "verblijfplaats__identificatiecodenummeraanduiding"
            in filters_values_dict
        )

    def get_filters_with_values(self):
        filters_with_values = dict()
        filter_keys = self.filter_class.get_filters().keys()
        for key in filter_keys:
            if self.request.GET.get(key):
                filters_with_values[key] = self.request.GET[key]

        # When retrieving a collection of people, one and only one of the six following combinations must be included
        # See combinations here
        #   https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/Bevragingen-ingeschreven-personen/master/specificatie/openapi.yaml#/ingeschrevenpersonen/ingeschrevenNatuurlijkPersonen
        if [
            self.combination_1(filters_with_values),
            self.combination_2(filters_with_values),
            self.combination_3(filters_with_values),
            self.combination_4(filters_with_values),
            self.combination_5(filters_with_values),
            self.combination_6(filters_with_values),
        ].count(True) != 1:
            raise ValidationError("Exactly one combination of filters must be supplied")

        return filters_with_values

    def list(self, request, *args, **kwargs):

        try:
            filters = self.get_filters_with_values()
        except ValidationError as e:
            return Response(data=e.detail[0], status=HTTP_400_BAD_REQUEST)

        data = StufBGClient.get_solo().get_persoon_request_data(filters=filters)

        return Response(data=data, status=HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):

        data = StufBGClient.get_solo().get_persoon_request_data(
            bsn=kwargs["burgerservicenummer"]
        )

        return Response(data=data, status=HTTP_200_OK)
