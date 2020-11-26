from .constants import *


def get_salutation_from_title(title):
    """
    Described here: https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/aanhef.feature#L4-L38
    """
    if title in ["Baron", "Hertog", "Jonkheer", "Markies", "Ridder"]:
        return HOOGWELGEBOREN_HEER
    if title in ["Barones", "Hertogin", "Jonkvrouw", "Markiezin"]:
        return HOOGWELGEBOREN_VROUWE
    if title in ["Prins", "Prinses"]:
        return HOOGHEID
    if title == "Graaf":
        return HOOGGEBOREN_HEER
    if title == "Gravin":
        return HOOGGEBOREN_VROUWE


def get_salutation_from_partner_title(title):
    """
    Described here: https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/aanhef.feature#L62-L71
    """
    if title in ["Baron", "Hertog", "Markies"]:
        return HOOGWELGEBOREN_VROUWE
    if title == "Graaf":
        return HOOGGEBOREN_VROUWE
    if title == "Prins":
        return HOOGHEID


def get_salutation_from_gender_designation(gender_designation):
    if gender_designation == "V":
        return GEACHTE_MEVROUW
    if gender_designation == "M":
        return GEACHTE_HEER


def get_aanhef_last_name(
    last_name_prefix,
    last_name,
    partner_last_name_prefix,
    partner_last_name,
    indication_name_use,
):
    aanhef_last_name = ""
    if indication_name_use == "E":  # Eigen
        if last_name_prefix:
            aanhef_last_name += f" {last_name_prefix.capitalize()}"
        aanhef_last_name += f" {last_name}"
    if indication_name_use == "N":  # Partner na eigen
        if last_name_prefix:
            aanhef_last_name += f" {last_name_prefix.capitalize()}"
        if last_name:
            aanhef_last_name += f" {last_name}-"
        else:
            aanhef_last_name += f" "
        if partner_last_name_prefix:
            aanhef_last_name += f"{partner_last_name_prefix} "
        if partner_last_name:
            aanhef_last_name += f"{partner_last_name}"
    if indication_name_use == "P":  # Partner
        if partner_last_name_prefix:
            aanhef_last_name += f" {partner_last_name_prefix.capitalize()}"
        aanhef_last_name += f" {partner_last_name}"
    if indication_name_use == "V":  # Partner voor eigen
        if partner_last_name_prefix:
            aanhef_last_name += f" {partner_last_name_prefix.capitalize()}"
        if partner_last_name:
            aanhef_last_name += f" {partner_last_name}-"
        else:
            aanhef_last_name += f" "
        if last_name_prefix:
            aanhef_last_name += f"{last_name_prefix} "
        if last_name:
            aanhef_last_name += f"{last_name}"

    return aanhef_last_name


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
    jonkheer_uses_partner_name = indication_name_use == "P" and title != "Jonkheer"
    jonkvrouw_with_partner = title == "Jonkvrouw" and (
        partner_last_name_prefix or partner_last_name
    )
    jonkvrouw_using_partner_name = title == "Jonkvrouw" and indication_name_use != "E"
    if (
        not jonkheer_uses_partner_name
        and not jonkvrouw_with_partner
        and not jonkvrouw_using_partner_name
    ):
        salutation = get_salutation_from_title(title)
        if salutation:
            return salutation

    if gender_designation == "V" and indication_name_use != "E":
        salutation = get_salutation_from_partner_title(partner_title)
        if salutation:
            return salutation

    salutation = get_salutation_from_gender_designation(gender_designation)
    if salutation:
        salutation += get_aanhef_last_name(
            last_name_prefix,
            last_name,
            partner_last_name_prefix,
            partner_last_name,
            indication_name_use,
        )

        return salutation

    return "string"
