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

    def rule_1(self, filters_values_dict):
        if filters_values_dict.get('geboorte__datum') and filters_values_dict.get('naam__geslachtsnaam'):
            return True

        filters_values_dict.pop('geboorte__datum', 0)
        filters_values_dict.pop('naam__geslachtsnaam', 0)

        return False

    def rule_2(self, filters_values_dict):
        if filters_values_dict.get('verblijfplaats__gemeentevaninschrijving') and \
            filters_values_dict.get('naam__geslachtsnaam'):
            return True

        filters_values_dict.pop('verblijfplaats__gemeentevaninschrijving', 0)
        filters_values_dict.pop('naam__geslachtsnaam', 0)

        return False

    def rule_3(self, filters_values_dict):
        return bool(filters_values_dict.get('burgerservicenummer'))

    def rule_4(self, filters_values_dict):
        if filters_values_dict.get('verblijfplaats__postcode') and \
            filters_values_dict.get('verblijfplaats__huisnummer'):
            return True

        filters_values_dict.pop('verblijfplaats__postcode', 0)
        filters_values_dict.pop('verblijfplaats__huisnummer', 0)

        return False

    def rule_5(self, filters_values_dict):
        if filters_values_dict.get('verblijfplaats__naamopenbareruimte') and \
            filters_values_dict.get('verblijfplaats__gemeentevaninschrijving') and \
            filters_values_dict.get('verblijfplaats__huisnummer'):
            return True

        filters_values_dict.pop('verblijfplaats__naamopenbareruimte', 0)
        filters_values_dict.pop('verblijfplaats__gemeentevaninschrijving', 0)
        filters_values_dict.pop('verblijfplaats__huisnummer', 0)

        return False

    def rule_6(self, filters_values_dict):
        return bool(filters_values_dict.get('verblijfplaats__identificatiecodenummeraanduiding'))

    def get_filters_with_values(self):
        filters_with_values = dict()
        filter_keys = self.filter_class.get_filters().keys()
        for key in filter_keys:
            if self.request.GET.get(key):
                filters_with_values[key] = self.request.GET[key]

        if not any([self.rule_1(filters_with_values), self.rule_2(filters_with_values),
                    self.rule_3(filters_with_values), self.rule_4(filters_with_values),
                    self.rule_5(filters_with_values), self.rule_6(filters_with_values)]):
            raise ValueError('Incorrect combination of filters')

        return filters_with_values

    def list(self, request, *args, **kwargs):

        try:
            filters = self.get_filters_with_values()
        except ValueError as e:
            return Response(data={'detail': str(e)}, status=HTTP_400_BAD_REQUEST)

        instances = IngeschrevenPersoon.retrieve(filters=filters)

        serializer = self.serializer_class(instances, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):

        burgerservicenummer = kwargs["burgerservicenummer"]

        instance = IngeschrevenPersoon.retrieve(burgerservicenummer)

        serializer = self.serializer_class(instance)

        return Response(data=serializer.data, status=HTTP_200_OK)
