from flask import Flask
from wanikanireverse import get_cards_from_database

app = Flask(__name__)

@app.route('/')
def everythings_file():
    return 'Everything is wonderful'

@app.route('/get_burned_cards')
def burned_cards():
    cards = get_cards_from_database()
    response = []
    for card in cards:
        response.append(card.json())
    return str(response)
