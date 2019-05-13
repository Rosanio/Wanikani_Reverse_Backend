import os
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

try:
    db_url = os.environ['DATABASE_URL']
except KeyError:
    db_url = 'postgresql://wanikanireverse:iinihongo@db:5432/wanikanireverse'
print("DATABASE URL: {}".format(db_url))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

try:
    from wanikanireverse import get_cards_from_database
except ImportError:
    from .wanikanireverse import get_cards_from_database

db.create_all()

@app.route('/', methods=['GET'])
def everythings_fine():
    return 'Everything is wonderful'

@app.route('/get_burned_cards', methods=['GET'])
def burned_cards():
    cards = get_cards_from_database()
    response = []
    for card in cards:
        response.append(card.json())
    return json.dumps(response, ensure_ascii=False)
