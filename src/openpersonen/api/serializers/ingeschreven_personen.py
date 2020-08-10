from rest_framework import serializers

from .datum import DatumSerializer
from .gezags_verhouding import GezagsVerhoudingSerializer
from .in_onderzoek import IngeschrevenPersoonInOnderzoekSerializer
from .kiesrecht import KiesrechtSerializer
from .nationaliteit import NationaliteitSerializer
from .opschorting_bijhouding import OpschortingBijhouding
from .overlijden import OverlijdenSerializer
from .persoon import PersoonSerializer
from .verblijf_plaats import VerblijfPlaatsSerializer
from .verblijfs_titel import VerblijfsTitelSerializer


class IngeschrevenPersoonSerializer(PersoonSerializer):
    leeftijd = serializers.IntegerField(min_value=0, max_value=999, required=False)
    datumEersteInschrijvingGBA = DatumSerializer(required=False)
    kiesrecht = KiesrechtSerializer(required=False)
    inOnderzoek = IngeschrevenPersoonInOnderzoekSerializer(required=False)
    nationaliteit = NationaliteitSerializer(many=True, required=False)
    opschortingBijhouding = OpschortingBijhouding(required=False)
    overlijden = OverlijdenSerializer(required=False)
    verblijfplaats = VerblijfPlaatsSerializer(required=False)
    gezagsverhouding = GezagsVerhoudingSerializer(required=False)
    verblijfstitel = VerblijfsTitelSerializer(required=False)
    reisdocumenten = serializers.ListField(child=serializers.CharField(max_length=9), required=False)
