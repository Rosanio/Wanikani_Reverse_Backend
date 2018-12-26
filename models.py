class Card:
    def __init__(self, japanese, english, character):
        self.uid = '{}:{}'.format(character, english)
        self.japanese = japanese
        self.english = english
        self.character = character

    def __repr__(self):
        return 'English: {} Japanese: {}'.format(self.english, self.character)

