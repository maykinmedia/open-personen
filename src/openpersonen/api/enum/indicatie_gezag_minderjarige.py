from djchoices import ChoiceItem, DjangoChoices


class IndicatieGezagMinderjarigeChoices(DjangoChoices):
    ouder1 = ChoiceItem('1', 'uder1')
    ouder2 = ChoiceItem('2', 'ouder2')
    derden = ChoiceItem('D', 'derden')
    ouder1_en_derde = ChoiceItem('1D', 'ouder1_en_derde')
    ouder2_en_derde = ChoiceItem('2D', 'ouder2_en_derde')
    ouder1_en_ouder2 = ChoiceItem('12', 'ouder1_en_ouder2')
