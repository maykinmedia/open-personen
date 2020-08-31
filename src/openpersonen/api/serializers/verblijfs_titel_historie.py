from rest_framework import serializers

from .verblijfs_titel import VerblijfsTitelSerializer


class VerblijfsTitelHistorieSerializer(VerblijfsTitelSerializer):
    geheimhoudingPersoonsgegevens = serializers.BooleanField(required=False)
