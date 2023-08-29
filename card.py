'''
Created on Jan 18, 2023

@author: willbrowne

This class models a singular playing card.
Attributes: the suit of the card and the value of the card
'''

class Card(object):
    card_names = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
    
    def __init__(self, suit: str, value: int):
        self.suit = suit
        self.value = value
        
    def name(self):
        return f"{Card.card_names[ self.value - 2 ]} of {self.suit}"
    
    def get_value(self):
        return self.value
    
    def get_suit(self):
        return self.suit

    def image_file_name(self):
        if self.value < 11:
            return f"{self.value}_of_{self.suit}.png"  
        else:
            return f"{Card.card_names[ self.value - 2 ].lower()}_of_{self.suit}.png"  