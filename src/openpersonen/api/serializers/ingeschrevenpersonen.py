from rest_framework import serializers

from .datum import DatumSerializer
from .gezagsverhouding import GezagsVerhoudingSerializer
from .inonderzoek import IngeschrevenPersoonInOnderzoekSerializer
from .kiesrecht import KiesrechtSerializer
from .nationaliteit import NationaliteitSerializer
from .opschortingbijhouding import OpschortingBijhouding
from .overlijden import OverlijdenSerializer
from .persoon import PersoonSerializer
from .verblijfplaats import VerblijfPlaatsSerializer
from .verblijfstitel import VerblijfsTitelSerializer


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
