#!/usr/bin/env bash

flask seed cards
gunicorn --reload --reload-engine auto -b 0.0.0.0:8001 main:app --log-file -
