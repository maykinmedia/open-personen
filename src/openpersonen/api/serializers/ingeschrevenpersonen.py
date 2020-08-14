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
    leeftijd = serializers.IntegerField()
    datumEersteInschrijvingGBA = DatumSerializer()
    kiesrecht = KiesrechtSerializer()
    inOnderzoek = IngeschrevenPersoonInOnderzoekSerializer()
    nationaliteit = NationaliteitSerializer(many=True)
    opschortingBijhouding = OpschortingBijhouding()
    overlijden = OverlijdenSerializer()
    verblijfplaats = VerblijfPlaatsSerializer()
    gezagsverhouding = GezagsVerhoudingSerializer()
    verblijfstitel = VerblijfsTitelSerializer()
    reisdocumenten = serializers.ListField(child=serializers.CharField())
