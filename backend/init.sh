#!/usr/bin/env bash

python manage.py fetch
gunicorn -b 0.0.0.0:8001 app:app --log-file -
