from dataclasses import dataclass


@dataclass
class Datum:
    dag: int
    datum: str
    jaar: int
    maand: int
