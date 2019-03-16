#!/usr/bin/env bash

 gunicorn -b 0.0.0.0:8001 backend.app:app --log-file -
