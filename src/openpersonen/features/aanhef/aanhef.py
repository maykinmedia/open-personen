from openpersonen.features.constants import *


def get_salutation_from_title(title):
    """
    Described here: https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/aanhef.feature#L4-L38
    """

    if title in [BARON, HERTOG, JONKHEER, MARKIES, RIDDER]:
        return HOOGWELGEBOREN_HEER
    if title in [BARONES, HERTOGIN, JONKVROUW, MARKIEZIN]:
        return HOOGWELGEBOREN_VROUWE
    if title in [PRINS, PRINSES]:
        return HOOGHEID
    if title == GRAAF:
        return HOOGGEBOREN_HEER
    if title == GRAVIN:
        return HOOGGEBOREN_VROUWE


def get_salutation_from_partner_title(title):
    """
    Described here: https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/aanhef.feature#L62-L71
    """
    if title in [BARON, HERTOG, MARKIES]:
        return HOOGWELGEBOREN_VROUWE
    if title == GRAAF:
        return HOOGGEBOREN_VROUWE
    if title == PRINS:
        return HOOGHEID


def get_salutation_from_gender_designation(gender_designation):
    if gender_designation == FEMALE:
        return GEACHTE_MEVROUW
    if gender_designation == MALE:
        return GEACHTE_HEER


def get_aanhef_last_name(
    last_name_prefix,
    last_name,
    partner_last_name_prefix,
    partner_last_name,
    indication_name_use,
):
    aanhef_last_name = ""
    if indication_name_use == EIGEN:
        if last_name_prefix:
            aanhef_last_name += f" {last_name_prefix.capitalize()}"
        aanhef_last_name += f" {last_name}"
    if indication_name_use == PARTNER_NA_EIGEN:
        if last_name_prefix:
            aanhef_last_name += f" {last_name_prefix.capitalize()}"

        aanhef_last_name += f" {last_name}-"

        if partner_last_name_prefix:
            aanhef_last_name += f"{partner_last_name_prefix} "

        aanhef_last_name += f"{partner_last_name}"
    if indication_name_use == PARTNER:
        if partner_last_name_prefix:
            aanhef_last_name += f" {partner_last_name_prefix.capitalize()}"
        aanhef_last_name += f" {partner_last_name}"
    if indication_name_use == PARTNER_VOOR_EIGEN:
        if partner_last_name_prefix:
            aanhef_last_name += f" {partner_last_name_prefix.capitalize()}"
        if partner_last_name:
            aanhef_last_name += f" {partner_last_name}-"
        else:
            aanhef_last_name += f" "
        if last_name_prefix:
            aanhef_last_name += f"{last_name_prefix} "

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
    jonkheer_uses_partner_name = indication_name_use == PARTNER and title != JONKHEER
    jonkvrouw_with_partner = title == JONKVROUW and (
        partner_last_name_prefix or partner_last_name
    )
    jonkvrouw_using_partner_name = title == JONKVROUW and indication_name_use != EIGEN
    if (
        not jonkheer_uses_partner_name
        and not jonkvrouw_with_partner
        and not jonkvrouw_using_partner_name
    ):
        salutation = get_salutation_from_title(title)
        if salutation:
            return salutation

    if gender_designation == FEMALE and indication_name_use != EIGEN:
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
