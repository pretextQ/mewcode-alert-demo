import logging

logger = logging.getLogger(__name__)


def fetch(client):
    # fix(REPLAY-B-03): upstream TimeoutError was unhandled and escaped fetch
    try:
        return client.get('/data')
    except TimeoutError as e:
        logger.warning('upstream timeout fetching /data: %s', e)
        return None
