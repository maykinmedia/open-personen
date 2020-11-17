from openpersonen.converters.api2stufbg.views.base import NestedViewSet


class OuderViewSet(NestedViewSet):
    backend_function_name = 'get_ouder'
