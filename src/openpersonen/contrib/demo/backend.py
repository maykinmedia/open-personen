
class BackEnd:

    def get_person(self, bsn=None, filters=None):
        if not bsn and not filters:
            raise ValueError('Either bsn or filters must be supplied')

        print('In get_person')

        return None

    def get_kind(self, bsn, kind_bsn=None):

        print('In get_kind')

        return None

    def get_ouder(self, bsn, ouder_bsn=None):
        print('In get_ouder')

        return None

    def get_partner(self, bsn, partner_bsn=None):
        print('In get_partner')

        return None
