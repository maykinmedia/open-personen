from dataclasses import dataclass


class Singleton(type):
    """
        Taken from https://stackoverflow.com/a/6798042
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


@dataclass
class ClientConfig(metaclass=Singleton):
    url: str
    headers: dict

    def __init__(self):
        self.url = 'https://httpbin.org/post'
        self.headers = {'Content-Type': 'application/xml'}


@dataclass
class Client:

    url: str
    headers: dict

    def __init__(self):
        config = ClientConfig()
        self.url = config.url
        self.headers = config.headers

    def get_gezinssituatie_op_adres_aanvrager(self, bsn):
        pass

    def get_kinderen_van_aanvrager(self, bsn):
        pass

    def get_natuurlijk_persoon(self, bsn):
        pass

    def get_vestiging(self, vestigings_nummer):
        pass
