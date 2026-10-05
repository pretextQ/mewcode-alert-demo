import app

class Client:
    def get(self, path):
        raise TimeoutError('upstream timed out')

try:
    app.fetch(Client())
except TimeoutError as e:
    print('unhandled_timeout: %r' % e); raise SystemExit(1)
print('ok: timeout handled')
