from djchoices import ChoiceItem, DjangoChoices


class OuderAanduiding(DjangoChoices):
    ouder1 = ChoiceItem('1', 'Ouder 1')
    ouder2 = ChoiceItem('2', 'Ouder 2')
