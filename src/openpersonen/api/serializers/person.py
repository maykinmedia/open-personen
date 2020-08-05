from rest_framework import serializers


class PersoonSerializer(serializers.Serializer):
    burgerservicenummer = serializers.CharField()
    geheimhoudingPersoonsgegevens = serializers.BooleanField()
    geslachtsaanduiding = serializers.CharField()
