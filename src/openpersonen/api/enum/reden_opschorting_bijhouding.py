from djchoices import ChoiceItem, DjangoChoices


class RedenOpschortingBijhoudingChoices(DjangoChoices):
    overlijden = ChoiceItem("overlijden", "overlijden")
    emigratie = ChoiceItem("emigratie", "emigratie")
    ministerieel_besluit = ChoiceItem("ministerieel_besluit", "Ministerieel Besluit")
    pl_aangelegd_in_de_rni = ChoiceItem(
        "pl_aangelegd_in_de_rni", "Pl Aangelegd In De Rni"
    )
    fout = ChoiceItem("fout", "Fout")
