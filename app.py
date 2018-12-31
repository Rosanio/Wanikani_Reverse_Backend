import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

try:
    db_url = os.environ['DATABASE_URL']
except KeyError:
    db_url = 'postgresql://wanikaniuser:iinihongo@127.0.0.1:5432/wanikanireverse'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

try:
    from wanikanireverse import get_cards_from_database
except ModuleNotFoundError:
    from .wanikanireverse import get_cards_from_database

db.create_all()

@app.route('/')
def everythings_file():
    return 'Everything is wonderful'

@app.route('/get_burned_cards')
@cross_origin()
def burned_cards():
    cards = get_cards_from_database()
    response = []
    for card in cards:
        print(card.__dict__)
        response.append(card.json())
    return str(response)
