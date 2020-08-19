from dataclasses import dataclass

from .datum import Datum


@dataclass
class OpschortingBijhouding:
    reden: str
    datum: Datum
