def owner_name(user):
    profile = user.get('profile')
    if not profile:
        return None
    return profile['name'].upper()
