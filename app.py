def owner_name(user):
    profile = user.get('profile') or {}
    name = profile.get('name')
    return name.upper() if name else ''
