import requests
from pprint import pprint
import sqlite3
import psycopg2
try:
    from models import Card
    from app import db
except ModuleNotFoundError:
    from .models import Card
    from .app import db

def get_burned_items():
    url = 'https://www.wanikani.com/api/user/d991e3214f6ad804b576e0a78de519af/vocabulary'
    response = requests.get(url)
    all_items = response.json()['requested_information']['general']
    return [item for item in all_items if item['user_specific'] is not None and item['user_specific']['burned']]

def create_cards_from_api(burned_items):
    cards = []
    for item in burned_items:
        card = Card(kana=item['kana'], english=item['meaning'], kanji=item['character'])
        cards.append(card)
    return cards

def add_cards_to_database(cards):
    for card in cards:
        existing_card = Card.query.filter_by(uid=card.uid).first()
        if not existing_card:
            db.session.add(card)
    db.session.commit()

def get_cards_from_database():
    cards = Card.query.all()
    return cards

def fetch_cards():
    print("Pulling info from WaniKani...")
    items = get_burned_items()
    print("Converting to cards...")
    cards = create_cards_from_api(items)
    print("Adding cards to database...")
    add_cards_to_database(cards)

