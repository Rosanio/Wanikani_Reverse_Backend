#!/usr/bin/env bash

python manage.py fetch
gunicorn --reload --reload-engine auto -b 0.0.0.0:8001 app:app --log-file -
