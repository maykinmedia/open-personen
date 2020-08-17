from djchoices import ChoiceItem, DjangoChoices


class SoortVerbintenis(DjangoChoices):
    huwelijk = ChoiceItem('huwelijk', 'Huwelijk')
    geregistreerd_partnerschap = ChoiceItem('geregistreerd_partnerschap', 'Geregistreerd Partnerschap')
