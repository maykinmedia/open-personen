from openpersonen.features.constants import *


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
        if last_name:
            gebruik_in_lopende_tekst += f" {last_name}-"
        else:
            gebruik_in_lopende_tekst += f" "
        if partner_last_name_prefix:
            gebruik_in_lopende_tekst += f"{partner_last_name_prefix} "
        if partner_last_name:
            gebruik_in_lopende_tekst += f"{partner_last_name}"
    if indication_name_use == PARTNER:
        if partner_last_name_prefix:
            gebruik_in_lopende_tekst += f" {partner_last_name_prefix.capitalize()}"
        gebruik_in_lopende_tekst += f" {partner_last_name}"
    if indication_name_use == PARTNER_VOOR_EIGEN:
        if partner_last_name_prefix:
            gebruik_in_lopende_tekst += f" {partner_last_name_prefix.capitalize()}"
        if partner_last_name:
            gebruik_in_lopende_tekst += f" {partner_last_name}-"
        else:
            gebruik_in_lopende_tekst += f" "
        if last_name_prefix:
            gebruik_in_lopende_tekst += f"{last_name_prefix} "
        if last_name:
            gebruik_in_lopende_tekst += f"{last_name}"

    return gebruik_in_lopende_tekst
