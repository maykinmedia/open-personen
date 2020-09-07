from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet


class BaseViewSet(ViewSet):

    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {"request": self.request, "format": self.format_kwarg, "view": self}

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.serializer_class
        kwargs["context"] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
