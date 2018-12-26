import requests
from pprint import pprint
import sqlite3
import psycopg2
from models import Card

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
                if parameters and parameters[i]:
                    cursor.execute(statement, parameters[i])
                else:
                    cursor.execute(statement)
            except(psycopg2.IntegrityError):
                conn.commit()
            finally:
                i += 1
        conn.commit()
    except(Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL ",error)
    finally:
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")

def create_cards(burned_items):
    cards = []
    for item in burned_items:
        card = Card(japanese=item['kana'], english=item['meaning'], character=item['character'])
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
    insert_query = """INSERT INTO cards VALUES (DEFAULT, %s, %s, %s, %s);"""
    insert_queries = []
    insert_params = []
    for card in cards:
        insert_queries.append(insert_query)
        insert_params.append((card.uid, card.japanese, card.english, card.character))
    execute_sql(insert_queries, insert_params)

reset_table()
burned_items = get_burned_items()
cards = create_cards(burned_items)
add_cards_to_database(cards)

