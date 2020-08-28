from djchoices import ChoiceItem, DjangoChoices


class AanduidingBijzonderNederlanderschapChoices(DjangoChoices):
    behandeld_als_nederlander = ChoiceItem(
        "behandeld_als_nederlander", "Behandeld Als Nederlander"
    )
    vastgesteld_niet_nederlander = ChoiceItem(
        "vastgesteld_niet_nederlander", "Vastgesteld Niet Nederlander"
    )
