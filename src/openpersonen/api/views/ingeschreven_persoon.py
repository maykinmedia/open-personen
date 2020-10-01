from django.core.exceptions import ObjectDoesNotExist

from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from openpersonen.api.data_classes import IngeschrevenPersoon
from openpersonen.api.filters import Backend, IngeschrevenPersoonFilter
from openpersonen.api.serializers import IngeschrevenPersoonSerializer
from openpersonen.api.views.auto_schema import OpenPersonenAutoSchema
from openpersonen.api.views.base import BaseViewSet
from openpersonen.api.views.generic_responses import RESPONSE_DATA_404


class IngeschrevenPersoonViewSet(BaseViewSet):

    lookup_field = "burgerservicenummer"
    lookup_value_regex = "[0-9]{9}"
    serializer_class = IngeschrevenPersoonSerializer
    filter_class = IngeschrevenPersoonFilter
    filter_backends = [
        Backend,
    ]

    def get_filter_parameters(self):
        return []

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

    @swagger_auto_schema(auto_schema=OpenPersonenAutoSchema)
    def list(self, request, *args, **kwargs):

        try:
            filters = self.get_filters_with_values()
        except ValidationError as e:
            return Response(data=e.detail[0], status=HTTP_400_BAD_REQUEST)

        instances = IngeschrevenPersoon.list(filters)

        serializer = self.serializer_class(instances, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)

    @swagger_auto_schema(auto_schema=OpenPersonenAutoSchema)
    def retrieve(self, request, *args, **kwargs):

        burgerservicenummer = kwargs["burgerservicenummer"]

        try:
            instance = IngeschrevenPersoon.retrieve(burgerservicenummer)
        except ObjectDoesNotExist:
            return Response(data=RESPONSE_DATA_404, status=HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(instance)

        return Response(data=serializer.data, status=HTTP_200_OK)
