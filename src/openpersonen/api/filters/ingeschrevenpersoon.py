from django_filters import filters
from vng_api_common.filtersets import FilterSet


class IngeschrevenPersoonFilter(FilterSet):
    geboorte__datum = filters.CharFilter()
    geboorte__plaats = filters.CharFilter()
    geslachtsaanduiding = filters.CharFilter()  # Add enum
    inclusiefoverledenpersonen = filters.BooleanFilter()
    naam__geslachtsnaam = filters.CharFilter()
    naam__voornamen = filters.CharFilter()
    verblijfplaats__gemeentevaninschrijving = filters.CharFilter()
    verblijfplaats__huisletter = filters.CharFilter()
    verblijfplaats__huisnummer = filters.NumberFilter()
    verblijfplaats__huisnummertoevoeging = filters.CharFilter()
    verblijfplaats__identificatiecodenummeraanduiding = filters.CharFilter()
    verblijfplaats__naamopenbareruimte = filters.CharFilter()
    verblijfplaats__postcode = filters.CharFilter()
    naam__voorvoegsel = filters.CharFilter()
