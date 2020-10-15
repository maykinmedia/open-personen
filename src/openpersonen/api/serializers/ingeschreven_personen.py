from django.urls import reverse

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
    def to_camel_case(snake_string):
        """
        Eg. Converts an_example_string to anExampleString
        """
        letters = snake_string.split("_")
        # Capitalize the first letter of each group of letters except the first one
        # with the 'title' method and join them together.
        return letters[0] + "".join(letter.title() for letter in letters[1:])

    def get_links_url(self, id, param):
        base_url = self.context['request'].build_absolute_uri().split('?')[0]

        if 'testserver' in base_url:
            base_url = base_url.replace('testserver', 'testserver.com')

        base_url += f'/{id}/{param}'
        return base_url

    def handle_dot_notation(self, param, representation, instance):
        for index, field_key in enumerate(param.split(".")[:-1]):
            if field_key not in representation:
                representation[field_key] = dict()

            attribute = param.split(".")[index + 1]
            attribute = self.to_camel_case(attribute)

            if not isinstance(instance, dict):
                fields = getattr(instance, field_key)
            else:
                fields = [instance]

            for field in fields:
                try:
                    if index + 2 == len(param.split(".")):
                        # At last value in dot notation so add to representation
                        representation[field_key][attribute] = field[attribute]
                        representation[field_key][param] = self.get_links_url(instance.burgerservicenummer, param.split(".")[0])
                    if attribute not in representation[field_key]:
                        # Add attribute to representation so that we can add
                        #   the nested value later
                        representation[field_key][attribute] = dict()
                    # Get next nested values
                    representation = representation[field_key]
                    instance = field[attribute]
                except KeyError:
                    raise ValueError(f"Invalid query param: {attribute}")

    def handle_expand_property(self, instance, representation):
        query_params = self.context["request"].GET["expand"].split(",")

        for param in query_params:
            if param.split(".")[0] not in self.expand_fields:
                raise ValueError(f"Invalid query param: {param}")

        for param in query_params:
            if "." in param:
                self.handle_dot_notation(param, representation, instance)
            else:
                attr = getattr(instance, param)
                representation[param] = attr
                representation[param][0][param] = self.get_links_url(instance.burgerservicenummer, param)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if "expand" in self.context["request"].GET:
            self.handle_expand_property(instance, representation)

        return representation
