from openpersonen.converters.api2stufbg.views.base import NestedViewSet


class PartnerViewSet(NestedViewSet):
    backend_template_name = "request/RequestPartner.xml"
