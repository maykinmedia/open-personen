from djchoices import ChoiceItem, DjangoChoices


class GeslachtsaanduidingChoices(DjangoChoices):
    man = ChoiceItem('M', 'Man')
    vrouw = ChoiceItem('V', 'Vrouw')
    onbekend = ChoiceItem('O', 'Onbekend')
