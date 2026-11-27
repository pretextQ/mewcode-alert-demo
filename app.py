TIMEOUT_SECONDS = 0


def configured_timeout():
    if TIMEOUT_SECONDS <= 0:
        raise ValueError("timeout must be positive")
    return TIMEOUT_SECONDS
