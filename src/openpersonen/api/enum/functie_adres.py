from djchoices import ChoiceItem, DjangoChoices


class FunctieAdresChoices(DjangoChoices):
    woonadres = ChoiceItem('woonadres', 'Woonadres')
    briefadres = ChoiceItem('briefadres', 'briefadres')
