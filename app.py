import logging

logger = logging.getLogger(__name__)


def fetch(client):
    try:
        return client.get('/data')
    except TimeoutError as exc:
        logger.warning("upstream timeout fetching /data: %s", exc)
        return None
