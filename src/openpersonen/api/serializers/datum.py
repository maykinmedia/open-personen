from rest_framework import serializers


class DatumSerializer(serializers.Serializer):
    dag = serializers.IntegerField()
    datum = serializers.CharField()
    jaar = serializers.IntegerField()
    maand = serializers.IntegerField()
