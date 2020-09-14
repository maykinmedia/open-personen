from openpersonen.api.data_classes import Ouder
from openpersonen.api.serializers import OuderSerializer
from openpersonen.api.views.base import NestedViewSet


class OuderViewSet(NestedViewSet):

    serializer_class = OuderSerializer
    instance_class = Ouder
