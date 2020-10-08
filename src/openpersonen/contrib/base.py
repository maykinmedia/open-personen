class BaseBackend:
    def get_person(self, bsn=None, filters=None):
        raise NotImplementedError

    def get_kind(self, bsn, id=None):
        raise NotImplementedError

    def get_ouder(self, bsn, id=None):
        raise NotImplementedError

    def get_partner(self, bsn, id=None):
        raise NotImplementedError
