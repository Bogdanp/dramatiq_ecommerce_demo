#!/usr/bin/env bash

set -e

rm -f db.sqlite3
python manage.py migrate
python manage.py loaddata fixtures/db.json
