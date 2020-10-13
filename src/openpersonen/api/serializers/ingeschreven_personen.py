from rest_framework import serializers

from openpersonen.api.enum import GeslachtsaanduidingChoices

from .datum import DatumSerializer
from .gezags_verhouding import GezagsVerhoudingSerializer
from .in_onderzoek import IngeschrevenPersoonInOnderzoekSerializer
from .kiesrecht import KiesrechtSerializer
from .naam import IngeschrevenPersoonNaamSerializer
from .nationaliteit import NationaliteitSerializer
from .opschorting_bijhouding import OpschortingBijhoudingSerializer
from .overlijden import OverlijdenSerializer
from .persoon import PersoonSerializer
from .verblijf_plaats import VerblijfPlaatsSerializer
from .verblijfs_titel import VerblijfsTitelSerializer


class IngeschrevenPersoonSerializer(PersoonSerializer):
    naam = IngeschrevenPersoonNaamSerializer(required=False)
    geslachtsaanduiding = serializers.ChoiceField(
        choices=GeslachtsaanduidingChoices.choices, required=False
    )
    leeftijd = serializers.IntegerField(max_value=999, required=False)
    datumEersteInschrijvingGBA = DatumSerializer(required=False)
    kiesrecht = KiesrechtSerializer(required=False)
    inOnderzoek = IngeschrevenPersoonInOnderzoekSerializer(required=False)
    nationaliteit = NationaliteitSerializer(many=True, required=False)
    opschortingBijhouding = OpschortingBijhoudingSerializer(required=False)
    overlijden = OverlijdenSerializer(required=False)
    verblijfplaats = VerblijfPlaatsSerializer(required=False)
    gezagsverhouding = GezagsVerhoudingSerializer(required=False)
    verblijfstitel = VerblijfsTitelSerializer(required=False)
    reisdocumenten = serializers.ListField(
        child=serializers.CharField(max_length=9), required=False
    )

    expand_fields = ["kinderen", "ouders", "partners"]

    @staticmethod
    def to_camel_case(snake_str):
        components = snake_str.split("_")
        # We capitalize the first letter of each component except the first one
        # with the 'title' method and join them together.
        return components[0] + "".join(x.title() for x in components[1:])

    def to_representation(self, instance):
        result = super().to_representation(instance)

        if "expand" in self.context["request"].GET:
            query_params = self.context["request"].GET["expand"].split(",")

            for param in query_params:
                if param.split(".")[0] not in self.expand_fields:
                    raise ValueError("Bad expand query params")

            for param in query_params:
                if "." in param:
                    if param.split(".")[0] not in result:
                        result[param.split(".")[0]] = dict()
                    field, attribute = param.split(".")
                    attribute = self.to_camel_case(attribute)
                    things = getattr(instance, field)
                    for thing in things:
                        try:
                            result[param.split(".")[0]][attribute] = thing[attribute]
                        except KeyError:
                            raise ValueError("Bad expand query params")
                else:
                    result[param] = getattr(instance, param)

        return result
