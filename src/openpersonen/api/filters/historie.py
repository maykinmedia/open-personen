from django_filters import filters
from vng_api_common.filtersets import FilterSet


class HistorieFilter(FilterSet):
    peildatum = filters.CharFilter()
    datumvan = filters.CharFilter()
    datumtotenmet = filters.CharFilter()

    @classmethod
    def get_filters_with_values(cls, request):
        filters_with_values = dict()
        filter_keys = cls.get_filters().keys()
        for key in filter_keys:
            if request.GET.get(key):
                filters_with_values[key] = request.GET[key]

        return filters_with_values
