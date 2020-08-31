from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ViewSet
from vng_api_common.filters import Backend

from openpersonen.api.data_classes import IngeschrevenPersoon
from openpersonen.api.filters import IngeschrevenPersoonFilter
from openpersonen.api.serializers import IngeschrevenPersoonSerializer


class IngeschrevenPersoonViewSet(ViewSet):

    lookup_field = "burgerservicenummer"
    serializer_class = IngeschrevenPersoonSerializer
    permission_classes = [IsAuthenticated]
    filter_class = IngeschrevenPersoonFilter
    filter_backends = [
        Backend,
    ]

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {"request": self.request, "format": self.format_kwarg, "view": self}

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.serializer_class
        kwargs["context"] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    @staticmethod
    def combination_1(filters_values_dict):
        return len(filters_values_dict) == 2 and 'geboorte__datum' in filters_values_dict and \
               'naam__geslachtsnaam' in filters_values_dict and len(filters_values_dict['naam__geslachtsnaam']) > 1

    @staticmethod
    def combination_2(filters_values_dict):
        return len(filters_values_dict) == 2 and 'verblijfplaats__gemeentevaninschrijving' in filters_values_dict and \
               'naam__geslachtsnaam' in filters_values_dict and len(filters_values_dict['naam__geslachtsnaam']) > 1

    @staticmethod
    def combination_3(filters_values_dict):
        return len(filters_values_dict) == 1 and 'burgerservicenummer' in filters_values_dict

    @staticmethod
    def combination_4(filters_values_dict):
        return len(filters_values_dict) == 2 and 'verblijfplaats__postcode' in filters_values_dict and \
               'verblijfplaats__huisnummer' in filters_values_dict

    @staticmethod
    def combination_5(filters_values_dict):
        return len(filters_values_dict) == 3 and 'verblijfplaats__gemeentevaninschrijving' in filters_values_dict and \
               'verblijfplaats__huisnummer' in filters_values_dict and \
               'verblijfplaats__naamopenbareruimte' in filters_values_dict and \
               len(filters_values_dict['verblijfplaats__naamopenbareruimte']) > 1

    @staticmethod
    def combination_6(filters_values_dict):
        return len(filters_values_dict) == 1 and \
               'verblijfplaats__identificatiecodenummeraanduiding' in filters_values_dict

    def get_filters_with_values(self):
        filters_with_values = dict()
        filter_keys = self.filter_class.get_filters().keys()
        for key in filter_keys:
            if self.request.GET.get(key):
                filters_with_values[key] = self.request.GET[key]

        # When retrieving a collection of people, one and only one of the six following combinations must be included
        # See combinations here
        #   https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/Bevragingen-ingeschreven-personen/master/specificatie/openapi.yaml#/ingeschrevenpersonen/ingeschrevenNatuurlijkPersonen
        if [self.combination_1(filters_with_values), self.combination_2(filters_with_values),
            self.combination_3(filters_with_values), self.combination_4(filters_with_values),
            self.combination_5(filters_with_values), self.combination_6(filters_with_values)].count(True) != 1:
                raise ValidationError('Exactly one combination of filters must be supplied')

        return filters_with_values

    def list(self, request, *args, **kwargs):

        try:
            filters = self.get_filters_with_values()
        except ValidationError as e:
            return Response(data=e.detail[0], status=HTTP_400_BAD_REQUEST)

        instances = IngeschrevenPersoon.list(filters)

        serializer = self.serializer_class(instances, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):

        burgerservicenummer = kwargs["burgerservicenummer"]

        instance = IngeschrevenPersoon.retrieve(burgerservicenummer)

        serializer = self.serializer_class(instance)

        return Response(data=serializer.data, status=HTTP_200_OK)
