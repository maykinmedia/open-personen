

def get_aanhef(persoon_dict):
    gender_designation = persoon_dict['geslachtsaanduiding']
    if gender_designation == "V":
        return "mevrouw"
    else:
        return "heer"
