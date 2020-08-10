from djchoices import ChoiceItem, DjangoChoices


class RedenOpschortingBijhoudingChoices(DjangoChoices):
    overlijden = ChoiceItem('O', 'overlijden')
    emigratie = ChoiceItem('E', 'emigratie')
    ministerieel_besluit = ChoiceItem('M', 'Ministerieel Besluit')
    pl_aangelegd_in_de_rni = ChoiceItem('R', 'Pl Aangelegd In De Rni')
    fout = ChoiceItem('F', 'Fout')
