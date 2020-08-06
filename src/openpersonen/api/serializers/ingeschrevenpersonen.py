from rest_framework import serializers

from .datum import DatumSerializer
from .gezagsverhouding import GezagsVerhoudingSerializer
from .inonderzoek import InOnderzoekSerializer
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
    inOnderzoek = InOnderzoekSerializer()
    nationaliteit = NationaliteitSerializer()
    opschortingBijhouding = OpschortingBijhouding()
    overlijden = OverlijdenSerializer()
    verblijfplaats = VerblijfPlaatsSerializer()
    gezagsverhouding = GezagsVerhoudingSerializer()
    verblijfstitel = VerblijfsTitelSerializer()
    reisdocumenten = serializers.ListField(child=serializers.CharField())
