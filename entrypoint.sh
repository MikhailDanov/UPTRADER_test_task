#!/bin/sh

python manage.py migrate && python manage.py loaddata fixture.json && exec "$@"