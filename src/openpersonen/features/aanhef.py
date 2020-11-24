def get_salutation_from_title(title):
    """
    Described here: https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/aanhef.feature#L4-L38
    """
    if title in ["Baron", "Hertog", "Jonkheer", "Markies", "Ridder"]:
        return "Hoogwelgeboren heer"
    if title in ["Barones", "Hertogin", "Jonkvrouw", "Markiezin"]:
        return "Hoogwelgeboren vrouwe"
    if title in ["Prins", "Prinses"]:
        return "Hoogheid"
    if title == "Graaf":
        return "Hooggeboren heer"
    if title == "Gravin":
        return "Hooggeboren vrouwe"


def get_salutation_from_partner_title(title):
    """
    Described here: https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/aanhef.feature#L62-L71
    """
    if title in ["Baron", "Hertog", "Markies"]:
        return "Hoogwelgeboren vrouwe"
    if title == "Graaf":
        return "Hooggeboren vrouwe"
    if title == "Prins":
        return "Hoogheid"


def get_salutation_from_gender_designation(gender_designation):
    if gender_designation == "V":
        return "Geachte mevrouw"
    if gender_designation == "M":
        return "Geachte heer"


def get_aanhef(last_name_prefix, last_name, gender_designation, title, partner_title):

    salutation = get_salutation_from_title(title)
    if salutation:
        return f"Geachte {salutation}"

    salutation = get_salutation_from_partner_title(partner_title)
    if salutation:
        return f"Geachte {salutation}"

    salutation = get_salutation_from_gender_designation(gender_designation)
    if salutation:
        if last_name_prefix:
            salutation += f" {last_name_prefix.capitalize()}"
        if last_name:
            salutation += f" {last_name}"
        return salutation

    return "string"
