def get_aanschrijfwijze_first_name(first_name):
    split_first_name = first_name.split(' ')
    aanschrijfwijze_first_name = ''

    for name in split_first_name:
        aanschrijfwijze_first_name += f'{name[0]}.'

    return aanschrijfwijze_first_name

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
    aanschrijfwijze = 'string'
    if indication_name_use == 'E':
        if last_name_prefix:
            aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {last_name_prefix} {last_name}"
        else:
            aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {last_name}"
    elif indication_name_use == 'N':
        if last_name_prefix and partner_last_name_prefix:
            aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {last_name_prefix} {last_name}-{partner_last_name_prefix} {partner_last_name}"
        else:
            aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {last_name}-{partner_last_name}"
    elif indication_name_use == 'P':
        if partner_last_name_prefix:
            aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {partner_last_name_prefix} {partner_last_name}"
        else:
            aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {partner_last_name}"
    elif indication_name_use == 'V':
        if last_name_prefix and partner_last_name_prefix:
            aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {partner_last_name_prefix} {partner_last_name}-{last_name_prefix} {last_name}"
        else:
            aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {partner_last_name}-{last_name}"

    return aanschrijfwijze
