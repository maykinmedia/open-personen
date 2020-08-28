from djchoices import ChoiceItem, DjangoChoices


class AanduidginBijHuisnummerChoices(DjangoChoices):
    tegenover = ChoiceItem("tegenover", "Tegenover")
    bij = ChoiceItem("bij", "Bij")
