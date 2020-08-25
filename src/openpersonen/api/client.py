import uuid
import requests
from django.conf import settings
from django.template import loader
from django.utils import timezone, dateformat


class Client:

    def _get_request_base_context(self):
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

    def _get_response_base_context(self):
        return {
            'zender_organisatie': settings.STUF_BG_ONTVANGER['organisatie'],
            'zender_applicatie': settings.STUF_BG_ONTVANGER['applicatie'],
            'zender_administratie': settings.STUF_BG_ONTVANGER['administratie'],
            'zender_gebruiker': settings.STUF_BG_ONTVANGER['gebruiker'],
            'ontvanger_organisatie': settings.STUF_BG_ZENDER['organisatie'],
            'ontvanger_applicatie': settings.STUF_BG_ZENDER['applicatie'],
            'ontvanger_administratie': settings.STUF_BG_ZENDER['administratie'],
            'ontvanger_gebruiker': settings.STUF_BG_ZENDER['gebruiker'],
        }

    def get_gezinssituatie_op_adres_aanvrager(self, bsn):
        request_context = self._get_request_base_context()
        request_context.update({'bsn': bsn})

        response = requests.post(settings.STUF_BG_URL,
                                 data=loader.render_to_string('RequestNatuurlijkPersoonSoapUIWithVariables.xml',
                                                              request_context),
                                 headers=settings.STUF_BG_HEADERS)

        response_context = self._get_response_base_context()
        request_context.update({'bsn': bsn})
        response_context['referentienummer'] = request_context['referentienummer']
        response_context['tijdstip_bericht'] = request_context['tijdstip_bericht']

        response._content = bytes(loader.render_to_string('ResponseNatuurlijkPersoonSoapUIWithVariables.xml',
                                                          response_context),
                                  encoding='utf-8')

        return response

    def get_kinderen_van_aanvrager(self, bsn):
        request_context = self._get_request_base_context()
        request_context.update({'bsn': bsn})

        response = requests.post(settings.STUF_BG_URL,
                                 data=loader.render_to_string('RequestNatuurlijkPersoonSoapUIWithVariables.xml',
                                                              request_context),
                                 headers=settings.STUF_BG_HEADERS)

        response_context = self._get_response_base_context()
        request_context.update({'bsn': bsn})
        response_context['referentienummer'] = request_context['referentienummer']
        response_context['tijdstip_bericht'] = request_context['tijdstip_bericht']

        response._content = bytes(loader.render_to_string('ResponseNatuurlijkPersoonSoapUIWithVariables.xml',
                                                          request_context),
                                  encoding='utf-8')

        return response

    def get_natuurlijk_persoon(self, bsn):
        request_context = self._get_request_base_context()
        request_context.update({'bsn': bsn})

        response = requests.post(settings.STUF_BG_URL,
                                 data=loader.render_to_string('RequestNatuurlijkPersoonSoapUIWithVariables.xml',
                                                              request_context),
                                 headers=settings.STUF_BG_HEADERS)

        response_context = self._get_response_base_context()
        request_context.update({'bsn': bsn})
        response_context['referentienummer'] = request_context['referentienummer']
        response_context['tijdstip_bericht'] = request_context['tijdstip_bericht']

        response._content = bytes(loader.render_to_string('ResponseNatuurlijkPersoonSoapUIWithVariables.xml',
                                                          response_context),
                                  encoding='utf-8')

        return response

    def get_vestiging(self, vestigings_nummer):
        request_context = self._get_request_base_context()
        request_context.update({'vestigings_nummer': vestigings_nummer})

        response = requests.post(settings.STUF_BG_URL,
                                 data=loader.render_to_string('RequestVestiging.xml',
                                                              request_context),
                                 headers=settings.STUF_BG_HEADERS)

        response_context = self._get_response_base_context()
        response_context.update({'vestigings_nummer': vestigings_nummer})
        response_context['referentienummer'] = request_context['referentienummer']
        response_context['tijdstip_bericht'] = request_context['tijdstip_bericht']

        response._content = bytes(loader.render_to_string('ResponseVestiging.xml',
                                                          response_context),
                                  encoding='utf-8')

        return response

    def get_ingeschreven_persoon(self, bsn):
        request_context = self._get_request_base_context()
        request_context.update({'bsn': bsn})

        response = requests.post(settings.STUF_BG_URL,
                                 data=loader.render_to_string('RequestIngeschrevenPersoon.xml',
                                                              request_context),
                                 headers=settings.STUF_BG_HEADERS)

        response_context = self._get_response_base_context()
        request_context.update({'bsn': bsn})
        response_context['referentienummer'] = request_context['referentienummer']
        response_context['tijdstip_bericht'] = request_context['tijdstip_bericht']

        response._content = bytes(loader.render_to_string('ResponseIngeschrevenPersoon.xml',
                                                          response_context),
                                  encoding='utf-8')

        return response

    def get_kind(self, bsn):
        request_context = self._get_request_base_context()
        request_context.update({'bsn': bsn})

        response = requests.post(settings.STUF_BG_URL,
                                 data=loader.render_to_string('RequestKind.xml',
                                                              request_context),
                                 headers=settings.STUF_BG_HEADERS)

        response_context = self._get_response_base_context()
        request_context.update({'bsn': bsn})
        response_context['referentienummer'] = request_context['referentienummer']
        response_context['tijdstip_bericht'] = request_context['tijdstip_bericht']

        response._content = bytes(loader.render_to_string('ResponseKind.xml',
                                                          response_context),
                                  encoding='utf-8')

        return response

    def get_ouder(self, bsn):
        request_context = self._get_request_base_context()
        request_context.update({'bsn': bsn})

        response = requests.post(settings.STUF_BG_URL,
                                 data=loader.render_to_string('RequestOuder.xml',
                                                              request_context),
                                 headers=settings.STUF_BG_HEADERS)

        response_context = self._get_response_base_context()
        request_context.update({'bsn': bsn})
        response_context['referentienummer'] = request_context['referentienummer']
        response_context['tijdstip_bericht'] = request_context['tijdstip_bericht']

        response._content = bytes(loader.render_to_string('ResponseOuder.xml',
                                                          response_context),
                                  encoding='utf-8')

        return response



client = Client()
