from djchoices import ChoiceItem, DjangoChoices


class AanduidginBijHuisnummerChoices(DjangoChoices):
    tegenover = ChoiceItem('to', 'Tegenover')
    bij = ChoiceItem('by', 'Bij')
