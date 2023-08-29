'''
Created on Jan 18, 2023

@author: willbrowne

This class models a poker hand of 5 playing cards.
Attributes: a "hand" (list) that receives cards as they are dealt
Major Algorithms:
print_hand() uses list comprehension to print the name of every card in the hand
add_card() this method uses a for loop, compares the card being added to other cards in the hand, and inserts the card in the correct, sorted order
rank() returns an integer number that corresponds to the hand's rank. Uses method decomposition by calling smaller methods to check for each type of hand.
get_hand_type() returns the ranking name, in English, that corresponds to the hand's rank
compare() compares two hands and determines a winner based on the rank. if the hands have the same rank, more detailed methods, often called inside the
larger method using method decomposition, are needed in order to confirm a winner.
List methods: .insert(), .sort()
'''

from card import Card

class Hand:
    
    def __init__(self):
        self.hand = []
        
    
    def get_hand(self):
        return self.hand
    
    def print_hand(self):
        [print(i.name()) for i in self.hand]
    
    def add_card(self, card: Card):
        self.hand.insert(0, card)
        self.hand.sort(key = get_value)
    
    def rank(self):
        if self.royal_flush():
            return 9
        if self.straight_flush():
            return 8
        if self.four_of_a_kind():
            return 7
        if self.full_house():
            return 6
        if self.flush():
            return 5
        if self.straight():
            return 4
        if self.three_of_a_kind():
            return 3
        if self.two_pair():
            return 2
        if self.one_pair():
            return 1
        if self.high_card():
            return 0
        
    def get_hand_type(self):
        if self.rank() == 9:
            return "royal flush"
        if self.rank() == 8:
            return "straight flush"
        if self.rank() == 7:
            return "four of a kind"
        if self.rank() == 6:
            return "full house"
        if self.rank() == 5:
            return "flush"
        if self.rank() == 4:
            return "straight"
        if self.rank() == 3:
            return "three of a kind"
        if self.rank() == 2:
            return "two pair"
        if self.rank() == 1:
            return "one pair"
        if self.rank() == 0:
            return "high card"
        
    def royal_flush(self):
        if (self.hand[0].get_value() == 10 and self.hand[1].get_value() == 11 and self.hand[2].get_value() == 12 and self.hand[3].get_value() == 13 and self.hand[4].get_value() == 14
            and self.hand[0].get_suit() == self.hand[1].get_suit() == self.hand[2].get_suit() == self.hand[3].get_suit() == self.hand[4].get_suit()):
            return True
        return False

    def straight_flush(self):
        if (self.hand[0].get_value() == self.hand[1].get_value() - 1 == self.hand[2].get_value() - 2 == self.hand[3].get_value() - 3 == self.hand[4].get_value() - 4
            and (self.hand[0].get_suit() == self.hand[1].get_suit() == self.hand[2].get_suit() == self.hand[3].get_suit() == self.hand[4].get_suit())):
            return True
        return False

    def four_of_a_kind(self):
        if (self.hand[0].get_value() == self.hand[3].get_value() or self.hand[1].get_value() == self.hand[4].get_value()):
            return True
        return False

    def full_house(self):
        if ((self.hand[0].get_value() == self.hand[1].get_value() and self.hand[2].get_value() == self.hand[4].get_value()) or 
            (self.hand[0].get_value() == self.hand[2].get_value() and self.hand[3].get_value() == self.hand[4].get_value())):
            return True
        return False
    
    def flush(self):
        if (self.hand[0].get_suit() == self.hand[1].get_suit() == self.hand[2].get_suit() == self.hand[3].get_suit() == self.hand[4].get_suit()):
            return True
        return False
    
    def straight(self):
        if (self.hand[0].get_value() == self.hand[1].get_value() - 1 == self.hand[2].get_value() - 2 == self.hand[3].get_value() - 3 == self.hand[4].get_value() - 4):
            return True
        return False
    
    def three_of_a_kind(self):
        if (self.hand[0].get_value() == self.hand[2].get_value() or self.hand[1].get_value() == self.hand[3].get_value() or self.hand[2].get_value() == self.hand[4].get_value()):
            return True
        return False
    
    def two_pair(self):
        if     ((self.hand[0].get_value() == self.hand[1].get_value() and self.hand[2].get_value() == self.hand[3].get_value())
             or (self.hand[0].get_value() == self.hand[1].get_value() and self.hand[3].get_value() == self.hand[4].get_value())
             or (self.hand[1].get_value() == self.hand[2].get_value() and self.hand[3].get_value() == self.hand[4].get_value())):
            return True
        return False
    
    def one_pair(self):
        if (self.hand[0].get_value() == self.hand[1].get_value() or self.hand[1].get_value() == self.hand[2].get_value() or 
            self.hand[2].get_value() == self.hand[3].get_value() or self.hand[3].get_value() == self.hand[4].get_value()):
            return True
        return False
    
    def high_card(self):
        if not(self.royal_flush() or self.straight_flush() or self.four_of_a_kind() or self.full_house() or self.flush() 
               or self.straight() or self.three_of_a_kind() or self.two_pair() or self.one_pair()):
            return True
        return False
    
    def compare_high_card(self, other_hand):
        if (self.hand[4].get_value() > other_hand.hand[4].get_value()):
            return 1
        elif (self.hand[4].get_value() < other_hand.hand[4].get_value()):
            return -1
        else:
            if (self.hand[3].get_value() > other_hand.hand[3].get_value()):
                return 1
            elif (self.hand[3].get_value() < other_hand.hand[3].get_value()):
                return -1
            else:
                if (self.hand[2].get_value() > other_hand.hand[2].get_value()):
                    return 1
                elif (self.hand[2].get_value() < other_hand.hand[2].get_value()):
                    return -1
                else:
                    if (self.hand[1].get_value() > other_hand.hand[1].get_value()):
                        return 1
                    elif (self.hand[1].get_value() < other_hand.hand[1].get_value()):
                        return -1
                    else:
                        if (self.hand[0].get_value() > other_hand.hand[0].get_value()):
                            return 1
                        elif (self.hand[0].get_value() < other_hand.hand[0].get_value()):
                            return -1
                        else:
                            return 0
                        
    def compare_one_pair(self, other_hand):
        if (self.hand[0].get_value() == self.hand[1].get_value()):
            sx = 0
        elif (self.hand[1].get_value() == self.hand[2].get_value()):
            sx = 1
        elif (self.hand[2].get_value() == self.hand[3].get_value()):
            sx = 2
        elif (self.hand[3].get_value() == self.hand[4].get_value()):
            sx = 3
        if (other_hand.hand[0].get_value() == other_hand.hand[1].get_value()):
            ox = 0
        elif (other_hand.hand[1].get_value() == other_hand.hand[2].get_value()):
            ox = 1
        elif (other_hand.hand[2].get_value() == other_hand.hand[3].get_value()):
            ox = 2
        elif (other_hand.hand[3].get_value() == other_hand.hand[4].get_value()):
            ox = 3
        if (self.hand[sx].get_value() > other_hand.hand[ox].get_value()):
            return 1
        elif (self.hand[sx].get_value() < other_hand.hand[ox].get_value()):
            return -1
        elif (self.hand[sx].get_value() == other_hand.hand[ox].get_value()):
            return self.compare_high_card(other_hand)
    
    def compare_two_pair(self, other_hand):
        if (self.hand[3].get_value() > other_hand.hand[3].get_value()):
            return 1
        elif (self.hand[3].get_value() < other_hand.hand[3].get_value()):
            return -1
        elif (self.hand[1].get_value() > other_hand.hand[1].get_value()):
            return 1
        elif (self.hand[1].get_value() < other_hand.hand[1].get_value()):
            return -1
        else:
            return self.compare_high_card(other_hand) 
    
    def compare_middle(self, other_hand):
        if (self.hand[2].get_value() > other_hand.hand[2].get_value()):
            return 1
        else:
            return -1
            
    def compare(self, other_hand):
        if (self.rank() > other_hand.rank()):
            return 1
        elif (other_hand.rank() > self.rank()):
            return -1
        elif (self.rank() == other_hand.rank()):
            if (self.royal_flush()):
                return 0
            elif (self.straight_flush() or self.flush() or self.straight() or self.high_card()):
                return self.compare_high_card(other_hand)
            elif (self.four_of_a_kind() or self.full_house() or self.three_of_a_kind()):
                return self.compare_middle(other_hand)
            elif (self.two_pair()):
                return self.compare_two_pair(other_hand)
            elif (self.one_pair()):
                return self.compare_one_pair(other_hand)
            
def get_value(obj):
    return obj.value
