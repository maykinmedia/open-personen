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


def get_aanhef(
    last_name_prefix,
    last_name,
    partner_last_name_prefix,
    partner_last_name,
    indication_name_use,
    gender_designation,
    title,
    partner_title,
):

    if indication_name_use == 'P' and title != 'Jonkheer':
        pass
    elif title == 'Jonkvrouw' and (partner_last_name_prefix or partner_last_name):
        pass
    elif title == 'Jonkvrouw' and indication_name_use != 'E':
        pass
    else:
        salutation = get_salutation_from_title(title)
        if salutation:
            return salutation

    salutation = get_salutation_from_partner_title(partner_title)
    if salutation:
        return salutation

    salutation = get_salutation_from_gender_designation(gender_designation)
    if salutation:
        if indication_name_use == "E":  # Eigen
            if last_name_prefix:
                salutation += f" {last_name_prefix.capitalize()}"
            if last_name:
                salutation += f" {last_name}"
        if indication_name_use == "N":  # Partner na eigen
            if last_name_prefix:
                salutation += f" {last_name_prefix.capitalize()}"
            if last_name:
                salutation += f" {last_name}-"
            if partner_last_name_prefix:
                salutation += f"{partner_last_name_prefix} "
            if partner_last_name:
                salutation += f"{partner_last_name}"
        if indication_name_use == "P":  # Partner
            if partner_last_name_prefix:
                if not partner_last_name_prefix[0].isupper():
                    partner_last_name_prefix = partner_last_name_prefix.capitalize()
                salutation += f" {partner_last_name_prefix}"
            if partner_last_name:
                salutation += f" {partner_last_name}"
        if indication_name_use == "V":  # Partner voor eigen
            if partner_last_name_prefix:
                salutation += f" {partner_last_name_prefix.capitalize()}"
            if partner_last_name:
                salutation += f" {partner_last_name}-"
            else:
                salutation += f" "
            if last_name_prefix:
                salutation += f"{last_name_prefix} "
            if last_name:
                salutation += f"{last_name}"

        return salutation

    return "string"
