try:
    from app import db
except ModuleNotFoundError:
    from .app import db

class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Text, unique=True, nullable=False)
    kana = db.Column(db.Text, nullable=False)
    english = db.Column(db.Text, nullable=False)
    kanji = db.Column(db.Text, nullable=False)

    def __init__(self, kana, english, kanji):
        self.uid = '{}:{}'.format(kanji, english)
        self.japanese = kana
        self.english = english
        self.character = kanji

    def __repr__(self):
        return 'English: {} Japanese: {}'.format(self.english, self.kanji)

    def json(self):
        return '{"kana": "%s", "kanji": "%s", "english": "%s"}' % (self.kana, self.kanji, self.english)

