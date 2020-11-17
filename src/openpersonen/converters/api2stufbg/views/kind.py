from openpersonen.converters.api2stufbg.views.base import NestedViewSet


class KindViewSet(NestedViewSet):
    backend_template_name = "request/RequestKind.xml"
