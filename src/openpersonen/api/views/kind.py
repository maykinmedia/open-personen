from openpersonen.api.data_classes import Kind
from openpersonen.api.serializers import KindSerializer
from openpersonen.api.views.base import NestedViewSet


class KindViewSet(NestedViewSet):

    lookup_field = "id"
    serializer_class = KindSerializer
    instance_class = Kind
