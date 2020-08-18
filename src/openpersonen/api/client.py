import uuid

import requests
from django.template import loader
from django.conf import settings
from django.utils import timezone, dateformat


class Client:

    def _get_base_context(self):
        return {
            'referentienummer': str(uuid.uuid4()),
            'tijdstip_bericht': dateformat.format(timezone.now(), 'YmdHis')
        }

    def get_gezinssituatie_op_adres_aanvrager(self, bsn):
        context_dict = self._get_base_context()
        context_dict.update({'bsn': bsn})

        requests.post(settings.STUF_BG_URL,
                      data=loader.render_to_string('GezinssituatieOpAdresAanvrager.xml', context_dict),
                      headers=settings.STUF_BG_HEADERS)

    def get_kinderen_van_aanvrager(self, bsn):
        context_dict = self._get_base_context()
        context_dict.update({'bsn': bsn})

        requests.post(settings.STUF_BG_URL,
                      data=loader.render_to_string('KinderenVanAanvrager.xml', context_dict),
                      headers=settings.STUF_BG_HEADERS)

    def get_natuurlijk_persoon(self, bsn):
        context_dict = self._get_base_context()
        context_dict.update({'bsn': bsn})

        requests.post(settings.STUF_BG_URL,
                      data=loader.render_to_string('NatuurlijkPersoon.xml', context_dict),
                      headers=settings.STUF_BG_HEADERS)

    def get_vestiging(self, vestigings_nummer):
        context_dict = self._get_base_context()
        context_dict.update({'vestigings_nummer': vestigings_nummer})

        requests.post(settings.STUF_BG_URL,
                      data=loader.render_to_string('Vestiging.xml', context_dict),
                      headers=settings.STUF_BG_HEADERS)
