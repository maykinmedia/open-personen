from dataclasses import dataclass

from .datum import Datum


class Kiesrecht:
    europeesKiesrecht: bool
    uitgeslotenVanKiesrecht: bool
    einddatumUitsluitingEuropeesKiesrecht: Datum
    einddatumUitsluitingKiesrecht: Datum
