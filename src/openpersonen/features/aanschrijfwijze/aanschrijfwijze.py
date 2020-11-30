from openpersonen.features.constants import *


def get_aanschrijfwijze_first_name(first_name):
    split_first_name = first_name.split(" ")
    aanschrijfwijze_first_name = ""

    for name in split_first_name:
        aanschrijfwijze_first_name += f"{name[0]}."

    return aanschrijfwijze_first_name


def get_aanschrijfwijze_with_title(
    last_name_prefix,
    last_name,
    first_name,
    partner_last_name_prefix,
    partner_last_name,
    indication_name_use,
    title,
):
    aanschrijfwijze = ""

    if indication_name_use == EIGEN:
        aanschrijfwijze = (
            f"{title.lower()} {get_aanschrijfwijze_first_name(first_name)}"
        )
        if last_name_prefix:
            aanschrijfwijze += f" {last_name_prefix}"
        aanschrijfwijze += f" {last_name}"
    elif indication_name_use == PARTNER_NA_EIGEN:
        aanschrijfwijze = (
            f"{title.lower()} {get_aanschrijfwijze_first_name(first_name)}"
        )
        if last_name_prefix:
            aanschrijfwijze += f" {last_name_prefix}"

        aanschrijfwijze += f" {last_name}-"

        if partner_last_name_prefix:
            aanschrijfwijze += f"{partner_last_name_prefix} "

        aanschrijfwijze += f"{partner_last_name}"
    elif indication_name_use == PARTNER_VOOR_EIGEN:
        aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)}"

        if partner_last_name_prefix:
            aanschrijfwijze += f" {partner_last_name_prefix}"

        aanschrijfwijze += f" {partner_last_name}-{title.lower()}"

        if last_name_prefix:
            aanschrijfwijze += f" {last_name_prefix}"

        aanschrijfwijze += f" {last_name}"

    return aanschrijfwijze


def get_aanschrijfwijze_based_on_partner_title(
    last_name_prefix,
    last_name,
    first_name,
    partner_last_name_prefix,
    partner_last_name,
    indication_name_use,
    partner_title,
):
    aanschrijfwijze = ""

    if indication_name_use == PARTNER_NA_EIGEN:
        aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)}"

        if last_name_prefix:
            aanschrijfwijze += f" {last_name_prefix}"

        aanschrijfwijze += (
            f" {last_name}-{MALE_TO_FEMALE_TITLES[partner_title].lower()}"
        )

        if partner_last_name_prefix:
            aanschrijfwijze += f" {partner_last_name_prefix}"

        aanschrijfwijze += f" {partner_last_name}"
    elif indication_name_use == PARTNER:
        aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {MALE_TO_FEMALE_TITLES[partner_title].lower()}"

        if partner_last_name_prefix:
            aanschrijfwijze += f" {partner_last_name_prefix}"

        aanschrijfwijze += f" {partner_last_name}"
    elif indication_name_use == PARTNER_VOOR_EIGEN:
        aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {MALE_TO_FEMALE_TITLES[partner_title].lower()}"

        if last_name_prefix and partner_last_name_prefix:
            aanschrijfwijze += f" {partner_last_name_prefix}"

        aanschrijfwijze += f" {partner_last_name}-"

        if last_name_prefix:
            aanschrijfwijze += f"{last_name_prefix} "

        aanschrijfwijze += f"{last_name}"

    return aanschrijfwijze


def get_default_aanschrijfwijze(
    last_name_prefix,
    last_name,
    first_name,
    partner_last_name_prefix,
    partner_last_name,
    indication_name_use,
):
    aanschrijfwijze = ""

    if indication_name_use == EIGEN:
        aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)}"

        if last_name_prefix:
            aanschrijfwijze += f" {last_name_prefix}"

        aanschrijfwijze += f" {last_name}"
    elif indication_name_use == PARTNER_NA_EIGEN:
        aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)}"

        if last_name_prefix:
            aanschrijfwijze += f" {last_name_prefix}"

        aanschrijfwijze += f" {last_name}-"

        if partner_last_name_prefix:
            aanschrijfwijze += f"{partner_last_name_prefix} "

        aanschrijfwijze += f"{partner_last_name}"
    elif indication_name_use == PARTNER:
        aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)}"

        if partner_last_name_prefix:
            aanschrijfwijze += f" {partner_last_name_prefix}"

        aanschrijfwijze += f" {partner_last_name}"
    elif indication_name_use == PARTNER_VOOR_EIGEN:
        aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)}"

        if partner_last_name_prefix:
            aanschrijfwijze += f" {partner_last_name_prefix}"

        aanschrijfwijze += f" {partner_last_name}-"

        if last_name_prefix:
            aanschrijfwijze += f"{last_name_prefix} "

        aanschrijfwijze += f"{last_name}"

    return aanschrijfwijze


def get_aanschrijfwijze(
    last_name_prefix,
    last_name,
    first_name,
    partner_last_name_prefix,
    partner_last_name,
    indication_name_use,
    gender_designation,
    title,
    partner_title,
):

    use_own_title = title in [JONKHEER, JONKVROUW] and indication_name_use != PARTNER
    title_based_on_partner = (
        partner_title in [BARON, PRINS]
        and gender_designation == FEMALE
        and indication_name_use != EIGEN
    )

    if use_own_title:
        aanschrijfwijze = get_aanschrijfwijze_with_title(
            last_name_prefix,
            last_name,
            first_name,
            partner_last_name_prefix,
            partner_last_name,
            indication_name_use,
            title,
        )
    elif title_based_on_partner:
        aanschrijfwijze = get_aanschrijfwijze_based_on_partner_title(
            last_name_prefix,
            last_name,
            first_name,
            partner_last_name_prefix,
            partner_last_name,
            indication_name_use,
            partner_title,
        )
    else:
        aanschrijfwijze = get_default_aanschrijfwijze(
            last_name_prefix,
            last_name,
            first_name,
            partner_last_name_prefix,
            partner_last_name,
            indication_name_use,
        )

    return aanschrijfwijze
