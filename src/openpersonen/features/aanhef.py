def get_saluation_from_title(title):
    """
    Described here: https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/aanhef.feature#L4-L38
    """
    if title == 'Baron':
        return 'Hoogwelgeboren heer'
    if title == 'Barones':
        return 'Hoogwelgeboren vrouwe'
    if title == 'Graaf':
        return 'Hooggeboren heer'
    if title == 'Gravin':
        return 'Hooggeboren vrouwe'
    if title == 'Hertog':
        return 'Hoogwelgeboren heer'
    if title == 'Hertogin':
        return 'Hoogwelgeboren vrouwe'
    if title == 'Jonkheer':
        return 'Hoogwelgeboren heer'
    if title == 'Jonkvrouw':
        return 'Hoogwelgeboren vrouwe'
    if title == 'Markies':
        return 'Hoogwelgeboren heer'
    if title == 'Markiezin':
        return 'Hoogwelgeboren vrouwe'
    if title == 'Prins':
        return 'Hoogheid'
    if title == 'Prinses':
        return 'Hoogheid'
    if title == 'Ridder':
        return 'Hoogwelgeboren heer'


def get_aanhef(persoon_dict, title):

    salutation = get_saluation_from_title(title)
    if salutation:
        return salutation

    gender_designation = persoon_dict['geslachtsaanduiding']
    if gender_designation == "V":
        return "mevrouw"
    if gender_designation == "M":
        return "heer"

    return "string"
