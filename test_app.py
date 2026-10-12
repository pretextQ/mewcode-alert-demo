import app
try:
    name = app.owner_name({'profile': None})
except Exception as e:
    print('null_deref crash: %r' % e); raise SystemExit(1)
print('ok:', name)
