from dataclasses import dataclass

from .waarde import Waarde


@dataclass
class VerblijfBuitenland:
    adresRegel1: str
    adresRegel2: str
    adresRegel3: str
    vertrokkenOnbekendWaarheen: bool
    land: Waarde
