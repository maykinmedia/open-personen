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
        if filters_values_dict.get('geboorte__datum') and filters_values_dict.get('naam__geslachtsnaam'):
            return True

        filters_values_dict.pop('geboorte__datum', 0)
        filters_values_dict.pop('naam__geslachtsnaam', 0)

        return False

    @staticmethod
    def combination_2(filters_values_dict):
        if filters_values_dict.get('verblijfplaats__gemeentevaninschrijving') and \
            filters_values_dict.get('naam__geslachtsnaam'):
            return True

        filters_values_dict.pop('verblijfplaats__gemeentevaninschrijving', 0)
        filters_values_dict.pop('naam__geslachtsnaam', 0)

        return False

    @staticmethod
    def combination_3(filters_values_dict):
        return bool(filters_values_dict.get('burgerservicenummer'))

    @staticmethod
    def combination_4(filters_values_dict):
        if filters_values_dict.get('verblijfplaats__postcode') and \
            filters_values_dict.get('verblijfplaats__huisnummer'):
            return True

        filters_values_dict.pop('verblijfplaats__postcode', 0)
        filters_values_dict.pop('verblijfplaats__huisnummer', 0)

        return False

    @staticmethod
    def combination_5(filters_values_dict):
        if filters_values_dict.get('verblijfplaats__naamopenbareruimte') and \
            filters_values_dict.get('verblijfplaats__gemeentevaninschrijving') and \
            filters_values_dict.get('verblijfplaats__huisnummer'):
            return True

        filters_values_dict.pop('verblijfplaats__naamopenbareruimte', 0)
        filters_values_dict.pop('verblijfplaats__gemeentevaninschrijving', 0)
        filters_values_dict.pop('verblijfplaats__huisnummer', 0)

        return False

    @staticmethod
    def combination_6(filters_values_dict):
        return bool(filters_values_dict.get('verblijfplaats__identificatiecodenummeraanduiding'))

    def get_filters_with_values(self):
        filters_with_values = dict()
        filter_keys = self.filter_class.get_filters().keys()
        for key in filter_keys:
            if self.request.GET.get(key):
                filters_with_values[key] = self.request.GET[key]

        # When retrieving a collection of people, at least one of the six following combinations must be included
        # See combinations here
        #   https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/Bevragingen-ingeschreven-personen/master/specificatie/openapi.yaml#/ingeschrevenpersonen/ingeschrevenNatuurlijkPersonen
        if not any([self.combination_1(filters_with_values), self.combination_2(filters_with_values),
                    self.combination_3(filters_with_values), self.combination_4(filters_with_values),
                    self.combination_5(filters_with_values), self.combination_6(filters_with_values)]):
            raise ValidationError('Incorrect combination of filters')

        return filters_with_values

    def list(self, request, *args, **kwargs):

        try:
            filters = self.get_filters_with_values()
        except ValidationError as e:
            return Response(data={'detail': str(e)}, status=HTTP_400_BAD_REQUEST)

        instances = IngeschrevenPersoon.list(filters)

        serializer = self.serializer_class(instances, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):

        burgerservicenummer = kwargs["burgerservicenummer"]

        instance = IngeschrevenPersoon.retrieve(burgerservicenummer)

        serializer = self.serializer_class(instance)

        return Response(data=serializer.data, status=HTTP_200_OK)
