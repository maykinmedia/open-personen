class BaseBackend:
    def get_person(self, bsn=None, filters=None):
        raise NotImplementedError

    def get_kind(self, bsn, id=None):
        raise NotImplementedError

    def get_ouder(self, bsn, id=None):
        raise NotImplementedError

    def get_partner(self, bsn, id=None):
        raise NotImplementedError

    def get_nationaliteit_historie(self, bsn, filters):
        raise NotImplementedError

    # def get_partner_historie(self, bsn, filters):
    #     raise NotImplementedError

    def get_verblijf_plaats_historie(self, bsn, filters):
        raise NotImplementedError

    def get_verblijfs_titel_historie(self, bsn, filters):
        raise NotImplementedError
