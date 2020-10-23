from rest_framework import serializers

from inflection import camelize

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
        base_url = self.context["request"].build_absolute_uri().split("?")[0]

        if id not in base_url:
            base_url += f"/{id}/{param}"
        else:
            base_url += f"/{param}"

        return base_url

    def handle_dot_notation(self, param, instance, representation):
        burgerservicenummer = instance.burgerservicenummer
        _object = instance
        split_params = param.split(".")

        for index, field_key in enumerate(split_params[:-1]):
            if field_key not in representation:
                representation[field_key] = dict()

            attribute = camelize(split_params[index + 1], False)

            fields = (
                getattr(_object, field_key) if not isinstance(_object, dict) else [_object]
            )

            for field in fields:
                try:
                    if attribute == split_params[-1]:
                        # At last value in dot notation so add to representation
                        representation[field_key][attribute] = field[attribute]
                        representation["url"] = self.get_links_url(
                            burgerservicenummer, split_params[0]
                        )
                    else:
                        # Get next nested values
                        representation = representation[field_key]
                        _object = field[attribute]
                except KeyError:
                    raise ValueError(param)

    def add_expand_data(self, instance, representation):
        query_params = self.context["request"].GET["expand"].split(",")

        for param in query_params:
            if param.split(".")[0] not in self.expand_fields:
                raise ValueError(param)
            elif "." in param:
                self.handle_dot_notation(param, instance, representation)
            else:
                representation[param] = getattr(instance, param)
                for expand_field in representation[param]:
                    expand_field["url"] = self.get_links_url(
                        instance.burgerservicenummer, expand_field
                    )

    def add_links(self, instance, representation):

        for field in self.expand_fields:
            representation[f"{field}_links"] = []
            for obj in getattr(instance, field):
                representation[f"{field}_links"].append(
                    {
                        "url": self.context["request"].build_absolute_uri(self.context["request"].path).replace(
                            f'/{instance.burgerservicenummer}', '')
                               + f"/{instance.burgerservicenummer}/{field}/{obj['burgerservicenummer']}"
                    }
                )

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if "expand" in self.context["request"].GET:
            self.add_expand_data(instance, representation)

        self.add_links(instance, representation)

        return representation
