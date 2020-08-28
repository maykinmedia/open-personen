from djchoices import ChoiceItem, DjangoChoices


class AanduidingNaamgebruikChoices(DjangoChoices):
    eigen = ChoiceItem("eigen", "Eigen")
    eigen_partner = ChoiceItem("eigen_partner", "Eigen Partner")
    partner = ChoiceItem("partner", "Partner")
    partner_eigen = ChoiceItem("partner_eigen", "Partner Eigen")
