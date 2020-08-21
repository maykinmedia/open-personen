import requests
from django.conf import settings
from django.template import loader
from django.utils import timezone, dateformat


class Client:

    def _get_request_base_context(self):
        return {
            'zender_organisatie': settings.STUF_BG_ZENDER['organisatie'],
            'zender_applicatie': settings.STUF_BG_ZENDER['applicatie'],
        }

    def _get_response_base_context(self):
        return {
            'zender_organisatie': settings.STUF_BG_ONTVANGER['organisatie'],
            'zender_applicatie': settings.STUF_BG_ONTVANGER['applicatie'],
            'ontvanger_organisatie': settings.STUF_BG_ZENDER['organisatie'],
            'ontvanger_applicatie': settings.STUF_BG_ZENDER['applicatie'],
            'tijdstip_bericht': dateformat.format(timezone.now(), 'YmdHis'),
        }

    def get_gezinssituatie_op_adres_aanvrager(self, bsn):
        request_context = self._get_request_base_context()
        request_context.update({'bsn': bsn})

        response = requests.post(settings.STUF_BG_URL,
                                 data=loader.render_to_string('RequestNatuurlijkPersoonSoapUIWithVariables.xml',
                                                              request_context),
                                 headers=settings.STUF_BG_HEADERS)

        response_context = self._get_response_base_context()
        response_context.update({'bsn': bsn})

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
        response_context.update({'bsn': bsn})

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
        response_context.update({'bsn': bsn})

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

        response._content = bytes(loader.render_to_string('ResponseVestiging.xml',
                                                          response_context),
                                  encoding='utf-8')

        return response


client = Client()
