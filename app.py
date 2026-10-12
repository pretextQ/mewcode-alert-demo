# fix(DemoBug): user['profile'] can be None, dereferencing it raised TypeError
def owner_name(user):
    profile = user.get('profile')
    if profile is None:
        return ''
    return profile['name'].upper()
