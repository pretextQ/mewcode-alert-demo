def owner_name(user):
    # fix(REPLAY-B-02): user['profile'] can be None, subscripting it raised TypeError
    profile = user.get('profile')
    if not profile:
        return None
    return profile['name'].upper()
