# poker README

# what does this project do?

Algorithms in this project are ones that would be used in a digital poker game. To be able to play a "mock" poker game through a computer, the program is able to deal cards randomly from a deck and differentiate between two (or more) hands of cards to determine a winner. 

# hand class

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

# deck class

This class models a deck of 52 playing cards.

Attributes: a "deck" (list) that stores all 52 cards

Major algorithms: 
print_deck() uses list comprehension to print the name of every card in the deck
shuffle() removes a card from a random index in the deck, adds it to the end of the list, and reverses the deck 1000 times
deal_card() if the deck isn't empty, this method "pops," or removes the first card in the deck and returns it

List methods: .append(), .remove(), .reverse(), .pop()

# card class

This class models a singular playing card.

Attributes: the suit of the card and the value of the card
