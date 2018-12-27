import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

try:
    from wanikanireverse import get_cards_from_database
except ModuleNotFoundError:
    from .wanikanireverse import get_cards_from_database

db.create_all()

@app.route('/')
def everythings_file():
    return 'Everything is wonderful'

@app.route('/get_burned_cards')
def burned_cards():
    cards = get_cards_from_database()
    response = []
    for card in cards:
        print(card.__dict__)
        response.append(card.json())
    return str(response)
