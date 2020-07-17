import click

from wanikanireverse import fetch_cards

def register(app):
    @app.cli.group()
    def seed():
        """Commands for bootstrapping the database"""

    @seed.command()
    def cards():
        fetch_cards()