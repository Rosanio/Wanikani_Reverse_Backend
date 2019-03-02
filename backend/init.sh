#!/usr/bin/env bash

 gunicorn backend.app:app --log-file -
