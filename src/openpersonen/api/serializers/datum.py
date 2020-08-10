from rest_framework import serializers


class DatumSerializer(serializers.Serializer):
    dag = serializers.IntegerField(min_value=1, max_value=31, required=False)
    datum = serializers.CharField(required=False)
    jaar = serializers.IntegerField(max_value=9999, required=False)
    maand = serializers.IntegerField(min_value=1, max_value=12, required=False)
