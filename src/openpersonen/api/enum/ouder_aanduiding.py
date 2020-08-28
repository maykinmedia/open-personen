from djchoices import ChoiceItem, DjangoChoices


class OuderAanduiding(DjangoChoices):
    ouder1 = ChoiceItem("ouder1", "Ouder 1")
    ouder2 = ChoiceItem("ouder2", "Ouder 2")
