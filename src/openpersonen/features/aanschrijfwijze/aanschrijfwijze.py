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

    use_own_name = (title in ['Jonkheer', 'Jonkvrouw'] and indication_name_use != 'P')

    if use_own_name:
        if indication_name_use == 'E':
            if last_name_prefix:
                aanschrijfwijze = f"{title.lower()} {get_aanschrijfwijze_first_name(first_name)} {last_name_prefix} {last_name}"
            else:
                aanschrijfwijze = f"{title.lower()} {get_aanschrijfwijze_first_name(first_name)} {last_name}"
        elif indication_name_use == 'N':
            if last_name_prefix and partner_last_name_prefix:
                aanschrijfwijze = f"{title.lower()} {get_aanschrijfwijze_first_name(first_name)} {last_name_prefix} {last_name}-{partner_last_name_prefix} {partner_last_name}"
            else:
                aanschrijfwijze = f"{title.lower()} {get_aanschrijfwijze_first_name(first_name)} {last_name}-{partner_last_name}"
        elif indication_name_use == 'V':
            if last_name_prefix and partner_last_name_prefix:
                aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {partner_last_name_prefix} {partner_last_name}-{title.lower()} {last_name_prefix} {last_name}"
            else:
                aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {partner_last_name}-{title.lower()} {last_name}"
    elif partner_title in ['Baron', 'Prins'] and gender_designation == 'V' and indication_name_use != 'E':
        if partner_title == 'Baron':
            title = 'barones'
        elif partner_title == 'Prins':
            title = 'prinses'
        if indication_name_use == 'N':
            if last_name_prefix and partner_last_name_prefix:
                aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {last_name_prefix} {last_name}-{title} {partner_last_name_prefix} {partner_last_name}"
            else:
                aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {last_name}-{title} {partner_last_name}"
        elif indication_name_use == 'P':
            if partner_last_name_prefix:
                aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {title} {partner_last_name_prefix} {partner_last_name}"
            else:
                aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {title} {partner_last_name}"
        elif indication_name_use == 'V':
            if last_name_prefix and partner_last_name_prefix:
                aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {title} {partner_last_name_prefix} {partner_last_name}-{last_name_prefix} {last_name}"
            else:
                aanschrijfwijze = f"{get_aanschrijfwijze_first_name(first_name)} {title} {partner_last_name}-{last_name}"
    else:
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
