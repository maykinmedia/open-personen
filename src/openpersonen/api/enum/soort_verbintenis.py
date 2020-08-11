from djchoices import ChoiceItem, DjangoChoices


class SoortVerbintenis(DjangoChoices):
    huwelijk = ChoiceItem('H', 'Huwelijk')
    geregistreerd_partnerschap = ChoiceItem('P', 'Geregistreerd Partnerschap')
