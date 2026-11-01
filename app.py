import logging

logger = logging.getLogger(__name__)


def fetch(client):
    try:
        return client.get('/data')
    except TimeoutError:
        logger.warning("upstream timed out fetching /data", exc_info=True)
        return None
