from djchoices import ChoiceItem, DjangoChoices


class AanduidingNaamgebruikChoices(DjangoChoices):
    eigen = ChoiceItem('E', 'Eigen')
    eigen_partner = ChoiceItem('N', 'Eigen Partner')
    partner = ChoiceItem('P', 'Partner')
    partner_eigen = ChoiceItem('V', 'Partner Eigen')
