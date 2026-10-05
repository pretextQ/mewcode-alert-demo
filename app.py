# fix(REPLAY-B-01): timeout config was 0, restored to 30s
TIMEOUT_SECONDS = 30


def timeout():
    return TIMEOUT_SECONDS
