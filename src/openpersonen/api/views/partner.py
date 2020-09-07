from openpersonen.api.data_classes import Partner
from openpersonen.api.serializers import PartnerSerializer
from openpersonen.api.views.base import NestedViewSet


class PartnerViewSet(NestedViewSet):

    lookup_field = "id"
    serializer_class = PartnerSerializer
    instance_class = Partner
