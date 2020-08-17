from djchoices import ChoiceItem, DjangoChoices


class IndicatieGezagMinderjarigeChoices(DjangoChoices):
    ouder1 = ChoiceItem('ouder1', 'Ouder 1')
    ouder2 = ChoiceItem('ouder2', 'Ouder 2')
    derden = ChoiceItem('derden', 'Derden')
    ouder1_en_derde = ChoiceItem('ouder1_en_derde', 'Ouder 1 en Derde')
    ouder2_en_derde = ChoiceItem('ouder2_en_derde', 'Ouder 2 en Derde')
    ouder1_en_ouder2 = ChoiceItem('ouder1_en_ouder2', 'Ouder 1 en Ouder 2')
