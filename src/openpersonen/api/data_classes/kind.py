from dataclasses import dataclass

from .in_onderzoek import KindInOnderzoek
from .persoon import Persoon


@dataclass
class Kind(Persoon):
    leeftijd: int
    inOnderzoek: KindInOnderzoek

    backend_function_name = "get_kind"
