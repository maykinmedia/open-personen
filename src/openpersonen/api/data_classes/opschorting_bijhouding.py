from dataclasses import dataclass

from openpersonen.api.enum import RedenOpschortingBijhoudingChoices
from .datum import Datum


@dataclass
class OpschortingBijhouding:
    reden: str
    datum: Datum

    def get_reden_display(self):
        return RedenOpschortingBijhoudingChoices.values[self.reden]
