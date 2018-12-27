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

def execute_sql(sql_statements, parameters=None):
    try:
        conn = psycopg2.connect(user='wanikaniuser',
                                password='iinihongo',
                                host='127.0.0.1',
                                port='5432',
                                database='wanikanireverse')
        print(conn.get_dsn_parameters(), '\n')
        cursor = conn.cursor()
        i = 0
        for statement in sql_statements:
            try:
                if parameters and len(parameters) > i:
                    cursor.execute(statement, parameters[i])
                else:
                    cursor.execute(statement)
            except(psycopg2.IntegrityError):
                conn.commit()
            finally:
                i += 1
        conn.commit()
        return cursor.fetchall()
    except(Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL ",error)
    finally:
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")

def create_cards_from_api(burned_items):
    cards = []
    for item in burned_items:
        card = Card(kana=item['kana'], english=item['meaning'], kanji=item['character'])
        cards.append(card)
    return cards

def reset_table():
    create_table_query = """CREATE TABLE IF NOT EXISTS cards
              (ID SERIAL PRIMARY KEY,
              UID TEXT UNIQUE NOT NULL,
              ENGLISH TEXT NOT NULL,
              JAPANESE TEXT NOT NULL,
              CHARACTER TEXT NOT NULL);"""
    sql = ['DROP TABLE cards', create_table_query]
    execute_sql(sql)

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

