'''
Created on Jan 18, 2023

@author: willbrowne

This class models a deck of 52 playing cards.
Attributes: a "deck" (list) that stores all 52 cards
Major algorithms: 
print_deck() uses list comprehension to print the name of every card in the deck
shuffle() removes a card from a random index in the deck, adds it to the end of the list, and reverses the deck 1000 times
deal_card() if the deck isn't empty, this method "pops," or removes the first card in the deck and returns it
List methods: .append(), .remove(), .reverse(), .pop()
'''
from card import Card
import random

class Deck:
    
    suits = ("hearts", "diamonds", "spades", "clubs")
    
    def __init__(self):
        self.deck = []
        for x in Deck.suits:
            for i in range(2, 15):
                self.deck.append(Card(x, i))
                
    def get_deck(self):
        return self.deck
    
    def print_deck(self):
        [print(i.name()) for i in self.deck]
    
    def shuffle(self):
        for i in range(1000):
            x = random.randint(0, 51)
            temp = self.deck[x]
            self.deck.remove(temp)
            self.deck.append(temp)
            self.deck.reverse()
            
    def deal_card(self):
        if (len(self.deck) == 0):
            return "None"
        else:
            top = self.deck[0]
            self.deck.pop(0)
            return top