import logging

logger = logging.getLogger(__name__)


def fetch(client):
    try:
        return client.get('/data')
    except TimeoutError:
        logger.warning("upstream timeout fetching path=%s", '/data')
        return None
