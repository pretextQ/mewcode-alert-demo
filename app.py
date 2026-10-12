def owner_name(user):
    # fix(DemoBug): profile can be null; dereferencing it crashed owner_name
    profile = user['profile']
    if profile is None:
        return None
    return profile['name'].upper()
