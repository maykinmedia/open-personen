from copy import deepcopy

from inflection import camelize
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

    def get_links_url(self, id=None, param=None):
        base_url = self.context["request"].build_absolute_uri().split("?")[0]

        if id and id not in base_url:
            base_url += f"/{id}"

        if param:
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
                getattr(_object, field_key)
                if not isinstance(_object, dict)
                else [_object]
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
                        instance.burgerservicenummer,
                        f"{param}/{expand_field['burgerservicenummer']}",
                    )

    def add_field_links(self, instance, representation, field):
        representation[f"{field}_links"] = []
        for obj in getattr(instance, field):
            representation[f"{field}_links"].append(
                {
                    "url": self.context["request"]
                    .build_absolute_uri(self.context["request"].path)
                    .replace(f"/{instance.burgerservicenummer}", "")
                    + f"/{instance.burgerservicenummer}/{field}/{obj['burgerservicenummer']}"
                }
            )

    def add_links(self, instance, representation):
        fields = self.context["request"].GET.get("fields")

        for expand_field in self.expand_fields:
            if fields:
                for field in fields.split(","):
                    # Only add if field is specified in `fields` parameter
                    if "_links" in field and expand_field == field.split(".")[1]:
                        self.add_field_links(instance, representation, expand_field)
            else:
                # No `fields` parameter supplied, simply add all fields
                self.add_field_links(instance, representation, expand_field)

    def handle_fields(self):

        fields_to_keep = []
        dot_fields_to_keep = dict()
        for field in self.context["request"].GET["fields"].split(","):
            if "_links" not in field:
                if "." in field:
                    field, nested_field = field.split(".")
                    fields_to_keep.append(field)
                    if field not in dot_fields_to_keep:
                        dot_fields_to_keep[field] = []
                    dot_fields_to_keep[field].append(nested_field)
                else:
                    fields_to_keep.append(field)
                if field not in self.fields:
                    raise ValueError(field)

        for field in deepcopy(self.fields.fields):
            if field not in fields_to_keep:
                self.fields.pop(field)

        for field, inner_fields in dot_fields_to_keep.items():
            for nested_field in deepcopy(self.fields[field].fields.fields):
                if nested_field not in inner_fields:
                    self.fields[field].fields.pop(nested_field)

    def to_representation(self, instance):

        if self.context["request"].GET.get("fields"):
            self.handle_fields()

        representation = super().to_representation(instance)

        if "expand" in self.context["request"].GET:
            self.add_expand_data(instance, representation)

        self.add_links(instance, representation)

        representation["url"] = self.get_links_url()

        return representation
