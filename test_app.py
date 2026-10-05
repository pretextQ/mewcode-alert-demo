import app
if app.timeout() <= 0:
    print('config_error: timeout is %r' % app.timeout()); raise SystemExit(1)
print('ok:', app.timeout())
