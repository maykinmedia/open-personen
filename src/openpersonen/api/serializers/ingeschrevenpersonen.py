from rest_framework import serializers

from .datum import DatumSerializer
from .geboorte import GeboorteSerializers
from .gezagsverhouding import GezagsVerhoudingSerializer
from .inonderzoek import InOnderzoekSerializer
from .kiesrecht import KiesrechtSerializer
from .naam import NaamSerializer
from .nationaliteit import NationaliteitSerializer
from .opschortingbijhouding import OpschortingBijhouding
from .overlijden import OverlijdenSerializer
from .person import PersoonSerializer
from .verblijfplaats import VerblijfPlaatsSerializer
from .verblijfstitel import VerblijfsTitelSerializer


class IngeschrevenPersoonSerializer(PersoonSerializer):
    leeftijd = serializers.IntegerField()
    datumEersteInschrijvingGBA = DatumSerializer()
    kiesrecht = KiesrechtSerializer()
    naam = NaamSerializer()
    inOnderzoek = InOnderzoekSerializer()
    nationaliteit = NationaliteitSerializer()
    geboorte = GeboorteSerializers()
    opschortingBijhouding = OpschortingBijhouding()
    overlijden = OverlijdenSerializer()
    verblijfplaats = VerblijfPlaatsSerializer()
    gezagsverhouding = GezagsVerhoudingSerializer()
    verblijfstitel = VerblijfsTitelSerializer()
    reisdocumenten = serializers.ListField(child=serializers.CharField())

