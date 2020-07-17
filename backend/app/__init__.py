#!/usr/bin/python3

import os
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DEFAULT_DATABASE_URL = 'postgresql://wanikanireverse:iinihongo@db:5432/wanikanireverse'

db = SQLAlchemy()

def create_app(test_config=None):
    try:
        db_url = os.environ['DATABASE_URL']
    except KeyError:
        db_url = DEFAULT_DATABASE_URL
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config is not None:
        app.config.update(test_config)

    initialize_extensions(app)
    return app

def initialize_extensions(app):
    db.init_app(app)
