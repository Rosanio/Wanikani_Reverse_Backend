#!/usr/bin/python3

import sys
print(sys.path)
from app import create_app, cli


app = create_app()
cli.register(app)

# try:
#     from wanikanireverse import get_cards_from_database
# except ImportError:
#     from .wanikanireverse import get_cards_from_database

# db.create_all()

# @app.route('/api', methods=['GET'])
# def everythings_fine():
#     return 'Everything is wonderful'

# @app.route('/api/get_burned_cards', methods=['GET'])
# def burned_cards():
#     cards = get_cards_from_database()
#     response = []
#     for card in cards:
#         response.append(card.json())
#     return json.dumps(response, ensure_ascii=False)
