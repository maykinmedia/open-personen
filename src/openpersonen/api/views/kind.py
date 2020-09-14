from openpersonen.api.data_classes import Kind
from openpersonen.api.serializers import KindSerializer
from openpersonen.api.views.base import NestedViewSet


class KindViewSet(NestedViewSet):

    serializer_class = KindSerializer
    instance_class = Kind
