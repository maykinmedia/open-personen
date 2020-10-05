import factory

from openpersonen.contrib.demo.models import Inschrijving

from .persoon import PersoonFactory


class InschrijvingFactory(factory.django.DjangoModelFactory):

    persoon = factory.SubFactory(PersoonFactory)
    datum_ingang_blokkering_pl = 20150614
    datum_opschorting_bijhouding = 20170912
    omschrijving_reden_opschorting_bijhouding = "E"
    datum_eerste_inschrijving_gba_rni = 20160825
    gemeente_waar_de_pk_zich_bevindt = 762
    indicatie_geheim = 0
    datum_verfificatie = 20190909
    omschrijving_verificatie = "Correctie adres"
    versienummer = 5
    datumtijdstempel = 20160901132009000
    pk_gegevens_volledig_meegeconverteerd = "P"
    rni_deelnemer = 401
    omschrijving_verdrag = ""

    class Meta:
        model = Inschrijving
