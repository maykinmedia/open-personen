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

        link_fields = []
        for field in self.context["request"].GET.get("fields", "").split(","):
            if "_links" in field:
                link_fields.append(field)

        for field in self.expand_fields:
            if link_fields:
                for link_field in link_fields:
                    if field in link_field.split(".")[1]:
                        self.add_field_links(instance, representation, field)
            else:
                self.add_field_links(instance, representation, field)

    def handle_fields(self):

        fields_to_keep = []
        dot_fields_to_keep = dict()
        for field in self.context["request"].GET["fields"].split(","):
            if "." in field:
                field_0, field_1 = field.split(".")
                fields_to_keep.append(field_0)
                if field_0 in dot_fields_to_keep:
                    dot_fields_to_keep[field_0].append(field_1)
                else:
                    dot_fields_to_keep[field_0] = [field_1]
            else:
                fields_to_keep.append(field)

        for field in fields_to_keep:
            if field != "_links" and field not in self.fields:
                raise ValueError(field)

        fields_to_remove = []
        for field in self.fields:
            if field not in fields_to_keep:
                fields_to_remove.append(field)

        for field in fields_to_remove:
            self.fields.pop(field)

        dot_fields_to_remove = dict()
        for field, inner_fields in dot_fields_to_keep.items():
            dot_fields_to_remove[field] = []
            try:
                for _field in self.fields[field].fields:
                    if _field not in inner_fields:
                        dot_fields_to_remove[field].append(_field)
            except KeyError:
                pass

        for field, inner_fields in dot_fields_to_remove.items():
            for _field in inner_fields:
                self.fields[field].fields.pop(_field)

    def to_representation(self, instance):

        if self.context["request"].GET.get("fields"):
            self.handle_fields()

        representation = super().to_representation(instance)

        if "expand" in self.context["request"].GET:
            self.add_expand_data(instance, representation)

        self.add_links(instance, representation)

        representation["url"] = self.get_links_url()

        return representation
