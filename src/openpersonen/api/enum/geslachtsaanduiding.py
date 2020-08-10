from djchoices import ChoiceItem, DjangoChoices


class GeslachtsaanduidingChoices(DjangoChoices):
    man = ChoiceItem('M', 'man')
    vrouw = ChoiceItem('V', 'vrouw')
    onbekend = ChoiceItem('O', 'onbekend')
