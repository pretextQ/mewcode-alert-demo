import logging

logger = logging.getLogger(__name__)


def fetch(client):
    try:
        return client.get('/data')
    except TimeoutError:
        logger.warning("fetch /data failed: upstream timed out")
        return None
