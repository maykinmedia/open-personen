from djchoices import ChoiceItem, DjangoChoices


class FunctieAdresChoices(DjangoChoices):
    woonadres = ChoiceItem('W', 'Woonadres')
    briefadres = ChoiceItem('B', 'briefadres')
