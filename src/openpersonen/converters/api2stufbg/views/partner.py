from openpersonen.converters.api2stufbg.views.base import NestedViewSet


class PartnerViewSet(NestedViewSet):
    backend_function_name = 'get_partner'
