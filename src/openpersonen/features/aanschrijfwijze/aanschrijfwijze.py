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
        aanschrijfwijze = f"{first_name[0]}. {last_name_prefix} {last_name}"
    elif indication_name_use == 'N':
        aanschrijfwijze = f"{first_name[0]}. {last_name_prefix} {last_name}-{partner_last_name_prefix} {partner_last_name}"
    elif indication_name_use == 'P':
        aanschrijfwijze = f"{first_name[0]}. {partner_last_name_prefix} {partner_last_name}"
    elif indication_name_use == 'V':
        aanschrijfwijze = f"{first_name[0]}. {partner_last_name_prefix} {partner_last_name}-{last_name_prefix} {last_name}"

    return aanschrijfwijze
