release: python manage.py migrate
web: daphne uchattut.asgi:application  --port 80 --bind 0.0.0.0 -v2
worker: python manage.py runworker --settings=uchattut.settings -v2 events
