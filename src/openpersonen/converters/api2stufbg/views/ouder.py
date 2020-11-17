from openpersonen.converters.api2stufbg.views.base import NestedViewSet


class OuderViewSet(NestedViewSet):
    backend_template_name = "request/RequestOuder.xml"
