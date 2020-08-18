import uuid

import requests
from django.conf import settings
from django.template import loader
from django.utils import timezone, dateformat


class Client:

    def _get_base_context(self):
        return {
            'zender_organisatie': settings.STUF_BG_ZENDER['organisatie'],
            'zender_applicatie': settings.STUF_BG_ZENDER['applicatie'],
            'zender_administratie': settings.STUF_BG_ZENDER['administratie'],
            'zender_gebruiker': settings.STUF_BG_ZENDER['gebruiker'],
            'ontvanger_organisatie': settings.STUF_BG_ONTVANGER['organisatie'],
            'ontvanger_applicatie': settings.STUF_BG_ONTVANGER['applicatie'],
            'ontvanger_administratie': settings.STUF_BG_ONTVANGER['administratie'],
            'ontvanger_gebruiker': settings.STUF_BG_ONTVANGER['gebruiker'],
            'referentienummer': str(uuid.uuid4()),
            'tijdstip_bericht': dateformat.format(timezone.now(), 'YmdHis')
        }

    def get_gezinssituatie_op_adres_aanvrager(self, bsn):
        context = self._get_base_context()
        context.update({'bsn': bsn})

        requests.post(settings.STUF_BG_URL,
                      data=loader.render_to_string('GezinssituatieOpAdresAanvrager.xml', context),
                      headers=settings.STUF_BG_HEADERS)

    def get_kinderen_van_aanvrager(self, bsn):
        context = self._get_base_context()
        context.update({'bsn': bsn})

        requests.post(settings.STUF_BG_URL,
                      data=loader.render_to_string('KinderenVanAanvrager.xml', context),
                      headers=settings.STUF_BG_HEADERS)

    def get_natuurlijk_persoon(self, bsn):
        context = self._get_base_context()
        context.update({'bsn': bsn})

        requests.post(settings.STUF_BG_URL,
                      data=loader.render_to_string('NatuurlijkPersoon.xml', context),
                      headers=settings.STUF_BG_HEADERS)

    def get_vestiging(self, vestigings_nummer):
        context = self._get_base_context()
        context.update({'vestigings_nummer': vestigings_nummer})

        requests.post(settings.STUF_BG_URL,
                      data=loader.render_to_string('Vestiging.xml', context),
                      headers=settings.STUF_BG_HEADERS)
