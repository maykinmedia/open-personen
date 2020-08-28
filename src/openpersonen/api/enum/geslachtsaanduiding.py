from djchoices import ChoiceItem, DjangoChoices


class GeslachtsaanduidingChoices(DjangoChoices):
    man = ChoiceItem("man", "Man")
    vrouw = ChoiceItem("vrouw", "Vrouw")
    onbekend = ChoiceItem("onbekend", "Onbekend")
