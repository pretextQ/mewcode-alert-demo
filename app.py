def owner_name(user):
    # fix(DemoBug): user['profile'] is nullable; guard the null deref before subscripting
    profile = user.get('profile')
    if not profile:
        return None
    name = profile.get('name')
    return name.upper() if name else None
