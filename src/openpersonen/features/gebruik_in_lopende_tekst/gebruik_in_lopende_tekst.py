from openpersonen.features.constants import *


def get_gebruik_in_lopende_tekst_with_title(
    last_name_prefix,
    last_name,
    partner_last_name_prefix,
    partner_last_name,
    indication_name_use,
    title,
):
    gebruik_in_lopende_tekst = title.lower()

    if indication_name_use == EIGEN:
        if last_name_prefix:
            gebruik_in_lopende_tekst += f" {last_name_prefix}"
        gebruik_in_lopende_tekst += f" {last_name}"
    if indication_name_use == PARTNER_NA_EIGEN:
        if last_name_prefix:
            gebruik_in_lopende_tekst += f" {last_name_prefix} "

        gebruik_in_lopende_tekst += f"{last_name}-"

        if partner_last_name_prefix:
            gebruik_in_lopende_tekst += f"{partner_last_name_prefix} "

        gebruik_in_lopende_tekst += f"{partner_last_name}"
    if indication_name_use == PARTNER:
        if partner_last_name_prefix:
            gebruik_in_lopende_tekst = f" {partner_last_name_prefix} "
        gebruik_in_lopende_tekst += f"{partner_last_name}"
    if indication_name_use == PARTNER_VOOR_EIGEN:
        if partner_last_name_prefix:
            gebruik_in_lopende_tekst += f" {partner_last_name_prefix} "
        gebruik_in_lopende_tekst += f"{partner_last_name}-"

        if last_name_prefix:
            gebruik_in_lopende_tekst += f"{last_name_prefix} "

        gebruik_in_lopende_tekst += f"{last_name}"

    return gebruik_in_lopende_tekst


def get_gebruik_in_lopende_tekst_with_predicate(
    last_name_prefix,
    last_name,
    partner_last_name_prefix,
    partner_last_name,
    indication_name_use,
    title,
):
    gebruik_in_lopende_tekst = ""

    if indication_name_use == EIGEN:
        gebruik_in_lopende_tekst = title.lower()
        if last_name_prefix:
            gebruik_in_lopende_tekst += f" {last_name_prefix} "
        gebruik_in_lopende_tekst += f"{last_name}"
    if indication_name_use == PARTNER_NA_EIGEN:
        gebruik_in_lopende_tekst = title.lower()
        if last_name_prefix:
            gebruik_in_lopende_tekst += f" {last_name_prefix} "

        gebruik_in_lopende_tekst += f"{last_name}-"

        if partner_last_name_prefix:
            gebruik_in_lopende_tekst += f"{partner_last_name_prefix} "

        gebruik_in_lopende_tekst += f"{partner_last_name}"
    if indication_name_use == PARTNER:
        if title == JONKHEER:
            gebruik_in_lopende_tekst = title.lower()
        else:
            gebruik_in_lopende_tekst = MEVROUW

        if partner_last_name_prefix:
            gebruik_in_lopende_tekst += f" {partner_last_name_prefix} "
        gebruik_in_lopende_tekst += f"{partner_last_name}"
    if indication_name_use == PARTNER_VOOR_EIGEN:
        if title == JONKHEER:
            gebruik_in_lopende_tekst = DE_HEER
        else:
            gebruik_in_lopende_tekst = MEVROUW

        if partner_last_name_prefix:
            gebruik_in_lopende_tekst += f" {partner_last_name_prefix} "
        if partner_last_name:
            gebruik_in_lopende_tekst += f"{partner_last_name}-"

        gebruik_in_lopende_tekst += f"{title.lower()} "

        if last_name_prefix:
            gebruik_in_lopende_tekst += f"{last_name_prefix} "

        gebruik_in_lopende_tekst += f"{last_name}"

    return gebruik_in_lopende_tekst


def get_gebruik_in_lopende_tekst_with_partner_title_or_predicate(
    last_name_prefix,
    last_name,
    partner_last_name_prefix,
    partner_last_name,
    indication_name_use,
    partner_title,
):

    if partner_title != JONKHEER and indication_name_use not in [
        EIGEN,
        PARTNER_NA_EIGEN,
    ]:
        gebruik_in_lopende_tekst = MALE_TO_FEMALE_TITLES[partner_title].lower()
    else:
        gebruik_in_lopende_tekst = MEVROUW

    if indication_name_use == EIGEN:
        if last_name_prefix:
            gebruik_in_lopende_tekst += f" {last_name_prefix} "
        gebruik_in_lopende_tekst += f"{last_name}"
    if indication_name_use == PARTNER_NA_EIGEN:
        if last_name_prefix:
            gebruik_in_lopende_tekst += f" {last_name_prefix} "

        gebruik_in_lopende_tekst += f"{last_name}-"

        if partner_title != JONKHEER and partner_title in MALE_TO_FEMALE_TITLES:
            gebruik_in_lopende_tekst += (
                f"{MALE_TO_FEMALE_TITLES[partner_title].lower()} "
            )

        if partner_last_name_prefix:
            gebruik_in_lopende_tekst += f"{partner_last_name_prefix} "

        gebruik_in_lopende_tekst += f"{partner_last_name}"
    if indication_name_use == PARTNER:
        if partner_last_name_prefix:
            gebruik_in_lopende_tekst += f" {partner_last_name_prefix} "
        gebruik_in_lopende_tekst += f"{partner_last_name}"
    if indication_name_use == PARTNER_VOOR_EIGEN:
        if partner_last_name_prefix:
            gebruik_in_lopende_tekst += f" {partner_last_name_prefix.capitalize()} "

        gebruik_in_lopende_tekst += f"{partner_last_name}-"

        if last_name_prefix:
            gebruik_in_lopende_tekst += f"{last_name_prefix} "

        gebruik_in_lopende_tekst += f"{last_name}"

    return gebruik_in_lopende_tekst


def get_default_gebruik_in_lopende_tekst(
    last_name_prefix,
    last_name,
    partner_last_name_prefix,
    partner_last_name,
    indication_name_use,
    gender_designation,
):
    gebruik_in_lopende_tekst = ""

    if gender_designation == MALE:
        gebruik_in_lopende_tekst = DE_HEER
    elif gender_designation == FEMALE:
        gebruik_in_lopende_tekst = MEVROUW

    if indication_name_use == EIGEN:
        if last_name_prefix:
            gebruik_in_lopende_tekst += f" {last_name_prefix.capitalize()}"
        gebruik_in_lopende_tekst += f" {last_name}"
    if indication_name_use == PARTNER_NA_EIGEN:
        if last_name_prefix:
            gebruik_in_lopende_tekst += f" {last_name_prefix.capitalize()}"

        gebruik_in_lopende_tekst += f" {last_name}-"

        if partner_last_name_prefix:
            gebruik_in_lopende_tekst += f"{partner_last_name_prefix} "

        gebruik_in_lopende_tekst += f"{partner_last_name}"
    if indication_name_use == PARTNER:
        if partner_last_name_prefix:
            gebruik_in_lopende_tekst += f" {partner_last_name_prefix.capitalize()}"
        gebruik_in_lopende_tekst += f" {partner_last_name}"
    if indication_name_use == PARTNER_VOOR_EIGEN:
        if partner_last_name_prefix:
            gebruik_in_lopende_tekst += f" {partner_last_name_prefix.capitalize()}"

        gebruik_in_lopende_tekst += f" {partner_last_name}-"

        if last_name_prefix:
            gebruik_in_lopende_tekst += f"{last_name_prefix} "

        gebruik_in_lopende_tekst += f"{last_name}"

    return gebruik_in_lopende_tekst


def get_gebruik_in_lopende_tekst(
    last_name_prefix,
    last_name,
    partner_last_name_prefix,
    partner_last_name,
    indication_name_use,
    gender_designation,
    title,
    partner_title,
):

    is_not_exclude_title = title not in [GRAAF, GRAVIN, JONKHEER, JONKVROUW]
    is_predicate = title in [JONKHEER, JONKVROUW]
    use_partner_title = partner_title and gender_designation != "M"

    if title and is_not_exclude_title:
        gebruik_in_lopende_tekst = get_gebruik_in_lopende_tekst_with_title(
            last_name_prefix,
            last_name,
            partner_last_name_prefix,
            partner_last_name,
            indication_name_use,
            title,
        )
    elif is_predicate:
        gebruik_in_lopende_tekst = get_gebruik_in_lopende_tekst_with_predicate(
            last_name_prefix,
            last_name,
            partner_last_name_prefix,
            partner_last_name,
            indication_name_use,
            title,
        )
    elif use_partner_title:
        gebruik_in_lopende_tekst = (
            get_gebruik_in_lopende_tekst_with_partner_title_or_predicate(
                last_name_prefix,
                last_name,
                partner_last_name_prefix,
                partner_last_name,
                indication_name_use,
                partner_title,
            )
        )
    else:
        gebruik_in_lopende_tekst = get_default_gebruik_in_lopende_tekst(
            last_name_prefix,
            last_name,
            partner_last_name_prefix,
            partner_last_name,
            indication_name_use,
            gender_designation,
        )

    return gebruik_in_lopende_tekst
