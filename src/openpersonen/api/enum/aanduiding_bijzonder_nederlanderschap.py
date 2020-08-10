from djchoices import ChoiceItem, DjangoChoices


class AanduidingBijzonderNederlanderschapChoices(DjangoChoices):
    behandeld_als_nederlander = ChoiceItem('B', 'Behandeld Als Nederlander')
    vastgesteld_niet_nederlander = ChoiceItem('V', 'Vastgesteld Niet Nederlander')
