import requests
from django.template import loader
from django.conf import settings


class Client:

    def get_gezinssituatie_op_adres_aanvrager(self, bsn):
        requests.post(settings.STUF_BG_URL,
                      data=loader.render_to_string('GezinssituatieOpAdresAanvrager.xml', {'bsn': bsn}),
                      headers=settings.STUF_BG_HEADERS)

    def get_kinderen_van_aanvrager(self, bsn):
        requests.post(settings.STUF_BG_URL,
                      data=loader.render_to_string('KinderenVanAanvrager.xml', {'bsn': bsn}),
                      headers=settings.STUF_BG_HEADERS)

    def get_natuurlijk_persoon(self, bsn):
        requests.post(settings.STUF_BG_URL,
                      data=loader.render_to_string('NatuurlijkPersoon.xml', {'bsn': bsn}),
                      headers=settings.STUF_BG_HEADERS)

    def get_vestiging(self, vestigings_nummer):
        requests.post(settings.STUF_BG_URL,
                      data=loader.render_to_string('Vestiging.xml', {'vestigingsNummer': vestigings_nummer}),
                      headers=settings.STUF_BG_HEADERS)
