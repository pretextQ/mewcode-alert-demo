import logging

logger = logging.getLogger(__name__)


def fetch(client):
    try:
        return client.get('/data')
    except TimeoutError as e:
        logger.error('app.fetch upstream timed out (%r)', e)
        return None
