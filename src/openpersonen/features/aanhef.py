def get_saluation_from_title(title):
    """
    Described here: https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/aanhef.feature#L4-L38
    """
    if title == "Baron":
        return "Hoogwelgeboren heer"
    if title == "Barones":
        return "Hoogwelgeboren vrouwe"
    if title == "Graaf":
        return "Hooggeboren heer"
    if title == "Gravin":
        return "Hooggeboren vrouwe"
    if title == "Hertog":
        return "Hoogwelgeboren heer"
    if title == "Hertogin":
        return "Hoogwelgeboren vrouwe"
    if title == "Jonkheer":
        return "Hoogwelgeboren heer"
    if title == "Jonkvrouw":
        return "Hoogwelgeboren vrouwe"
    if title == "Markies":
        return "Hoogwelgeboren heer"
    if title == "Markiezin":
        return "Hoogwelgeboren vrouwe"
    if title == "Prins":
        return "Hoogheid"
    if title == "Prinses":
        return "Hoogheid"
    if title == "Ridder":
        return "Hoogwelgeboren heer"


def get_saluation_from_partner_title(title):
    """
    Described here: https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/aanhef.feature#L62-L71
    """
    if title == "Baron":
        return "Hoogwelgeboren vrouwe"
    if title == "Graaf":
        return "Hooggeboren vrouwe"
    if title == "Hertog":
        return "Hoogwelgeboren vrouwe"
    if title == "Markies":
        return "Hoogwelgeboren vrouwe"
    if title == "Prins":
        return "Hoogheid"


def get_aanhef(persoon_dict, title, partner_title):

    salutation = get_saluation_from_title(title)
    if salutation:
        return f"Geachte {salutation}"

    salutation = get_saluation_from_partner_title(partner_title)
    if salutation:
        return f"Geachte {salutation}"

    gender_designation = persoon_dict["geslachtsaanduiding"]
    if gender_designation == "V":
        return "Geachte mevrouw"
    if gender_designation == "M":
        return "Geachte heer"

    return "string"
