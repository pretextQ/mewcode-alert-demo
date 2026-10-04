def fetch(client):
    try:
        return client.get('/data')
    except TimeoutError:
        return None
